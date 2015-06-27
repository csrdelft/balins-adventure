var Q = require('q-xhr')(window.XMLHttpRequest, require('q'));

var api = 'http://localhost:8000/api/v1';

// api functions
module.exports = {
  forum: {
    get_recent : (n=5) => {
      return Q.xhr
        .get(api + '/forum/recent', {
          params: { 'n': n }
        });
    }
  }
};
