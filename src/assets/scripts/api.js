var Q = require('q-xhr')(window.XMLHttpRequest, require('q'));

var api = 'http://localhost:8000/api/v1';

// api functions
var api_obj = {

  // the forum resource
  forum: {

    // query the n most recent forum posts
    get_recent : (n=5) => {
      return Q.xhr
        .get(api + '/forum/draad/recent', {
          params: { n: n }
        });
    },

    draad : {
      // get the metadata for the draad endpoint
      metadata : (pk) => {
        return Q.xhr({
          method: 'options',
          url: api + '/forum/draad/' + pk + '/'
        });
      }
    }
  },

  // the auth and base resources
  base: {

    get_profiel: (id) => {
      return Q.xhr
        .get(api + "/profiel/" + id);
    }

  },

  maaltijden: {

    get_upcoming: (at) => {
      return Q.xhr
        .get(api + "/maaltijden/", {
          params: { at: at }
        });
    },

    aanmelden: (id, gasten=0, gasten_eetwens="") => {
      return Q.xhr
        .post(api + "/maaltijden/" + id + "/aanmelden/", {
           aantal_gasten: gasten,
           gasten_eetwens: gasten_eetwens
        });
    },

    afmelden: (id) => {
      return Q.xhr
        .post(api + "/maaltijden/" + id + "/afmelden/");
    },
  }
};

// make api available globally
window.api = api_obj;

module.exports = api_obj;
