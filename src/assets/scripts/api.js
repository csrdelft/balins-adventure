var Q = require('q-xhr')(window.XMLHttpRequest, require('q'));
var Cookies = require('cookies-js');

var api = '/api/v1';

// api functions
var api_obj = {

  // the forum resource
  forum: {

    // get subfora
    list: (page=1, page_size=25) => {
      return Q.xhr
          .get(`${api}/forum/parts/`, {
            params: {
              page_size: page_size,
              page: page
            }
          });
    },

    threads : {
      // query the n most recent forum posts
      get_recent: (n = 5) => {
        return Q.xhr
          .get(`${api}/forum/threads/recent`, {
            params: {n: n}
          });
      },

      get: (pk) => {
        return Q.xhr
          .get(`${api}/forum/threads/${pk}`);
      },

      list: (forum=undefined, page=1, page_size=25) => {
        return Q.xhr
          .get(`${api}/forum/threads/`, {
            params: {
              forum: forum,
              page_size: page_size,
              page: page
            }
          });
      },

      // create a new forum draadje
      create: (data) => {
        return Q.xhr
          .post(`${api}/forum/threads/`, data, {
            headers: {
              'X-CSRFToken': Cookies.get('csrftoken')
            }
          });
      },

      // get the metadata for the draad endpoint
      metadata : (pk) => {
        return Q.xhr({
          method: 'options',
          url: api + '/forum/threads/' + pk + '/'
        });
      }
    }
  },

  // the auth and base resources
  profiel: {

    get: (pk) => {
      return Q.xhr
        .get(`${api}/profiel/${pk}`);
    }

  },

  maaltijden: {

    get_upcoming: (at) => {
      return Q.xhr
        .get(`${api}/maaltijden/`, {
          params: {at: at}
        });
    },

    aanmelden: (pk, gasten = 0, gasten_eetwens = "") => {
      return Q.xhr
        .post(`${api}/maaltijden/${pk}/aanmelden/`, {
          aantal_gasten: gasten,
          gasten_eetwens: gasten_eetwens
        });
    },

    afmelden: (pk) => {
      return Q.xhr
        .post(`${api}/maaltijden/${pk}/afmelden/`);
    },
  },

  mededelingen: {
    list: () => {
      return Q.xhr
        .get(`${api}/mededelingen/`);
    },

    get: (pk) => {
      return Q.xhr
        .get(`${api}/mededelingen/${pk}/`);
    }
  }
};

// make api available globally
window.api = api_obj;

module.exports = api_obj;
