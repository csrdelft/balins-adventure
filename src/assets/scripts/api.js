var Q = require('q-xhr')(window.XMLHttpRequest, require('q'));

var api = 'http://localhost:8000/api/v1';

// api functions
module.exports = {

  // the forum resource
  forum: {

    // query the n most recent forum posts
    get_recent : (n=5) => {
      return Q.xhr
        .get(api + '/forum/recent', {
          params: { 'n': n }
        });
    }

  },

  // the auth and base resources
  base: {

    get_profiel: (id) => {
      return Q.xhr
        .get(api + "/profiel/" + id);
    }

  }
};
