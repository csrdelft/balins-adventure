var Q = require('q-xhr')(window.XMLHttpRequest, require('q'));

var api = '/api/v1';

// api functions
var api_obj = {

  // the forum resource
  forum: {

    // query the n most recent forum posts
    get_recent: (n = 5) => {
      return Q.xhr
        .get(`${api}/forum/recent`, {
          params: {n: n}
        });
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
