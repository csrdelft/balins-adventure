var Q = require('q-xhr')(window.XMLHttpRequest, require('q'));
var Cookies = require('cookies-js');

var api = '/api/v1';

// api functions
var api_obj = {

  // the forum resource
  forum: {

    threads : {
      // query the n most recent forum posts
      get_recent: (n = 5) => {
        return Q.xhr
          .get(`${api}/forum/threads/recent`, {
            params: {n: n}
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
  base: {

    get_profiel: (id) => {
      return Q.xhr
        .get(`${api}/profiel/${id}`);
    }

  },

  maaltijden: {

    get_upcoming: (at) => {
      return Q.xhr
        .get(`${api}/maaltijden/`, {
          params: {at: at}
        });
    },

    aanmelden: (id, gasten = 0, gasten_eetwens = "") => {
      return Q.xhr
        .post(`${api}/maaltijden/${id}/aanmelden/`, {
          aantal_gasten: gasten,
          gasten_eetwens: gasten_eetwens
        });
    },

    afmelden: (id) => {
      return Q.xhr
        .post(`${api}/maaltijden/${id}/afmelden/`);
    },
  },

  mededelingen: {
    get_list: () => {
      return Q.xhr
        .get(`${api}/mededelingen/`);
    },

    get_mededeling: (id) => {
      return Q.xhr
        .get(`${api}/mededelingen/${id}/`);
    }
  }
};

// make api available globally
window.api = api_obj;

module.exports = api_obj;
