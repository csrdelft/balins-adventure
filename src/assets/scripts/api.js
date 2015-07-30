let Q = require('q-xhr')(window.XMLHttpRequest, require('q'));
let Cookies = require('cookies-js');
let _ = require('underscore');

let api = '/api/v1';

Q.xhr.interceptors = [
  // interceptor to load the url parameters into the url
  // while keeping track of them in the 'params' field of the config.
  // this is useful to be able to recover the url parameters easily from the response
  // in the listeners
  {
    request: (config) => {
      config.urlparams = {};

      _.each(config.params, (param, name) => {
        if(config.url.indexOf(`:${name}`) !== -1) {
          config.url = config.url.replace(`:${name}`, param.toString());

          // prevent it from showing up in the get params
          delete config.params[name];
          // back the value up
          config.urlparams[name] = param;
        }
      });

      return config;
    },

    response: (resp) => {
      // put the urlparams back in the params
      _.extend(resp.config.params, resp.config.urlparams);
      return resp;
    }
  }
];

//
// utility functions
//

function post(url, data, options={}) {
  options.headers = _.defaults(options.headers || {}, {
    'X-CSRFToken': Cookies.get('csrftoken')
  });

  return Q.xhr.post(url, data, options);
}

function del(url, options={}) {
  options.headers = _.defaults(options.headers || {}, {
    'X-CSRFToken': Cookies.get('csrftoken')
  });

  return Q.xhr.delete(url, options);
}

//
// api functions
//

let api_obj = {

  login: (data) => post(`${api}/login`, data),

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

      get: (pk, page=1, page_size=25) => {
        return Q.xhr
          .get(`${api}/forum/threads/:pk`, {
            params: {
              page_size: page_size,
              page: page,
              pk: pk
            }
          });
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
      create: (data) => post(`${api}/forum/threads/`, data),

      // delete a forum draadje
      delete: (pk) => del(`${api}/forum/threads/:pk`, { params: {pk: pk}}),
    },

    posts: {
      // create a new forum post
      create: (data) => post(`${api}/forum/posts/`, data),
    }

  },

  // the auth and base resources
  profiel: {

    get: (pk) => {
      return Q.xhr
        .get(`${api}/profiel/:pk`, {
          params: {pk: pk}
        });
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
        .post(`${api}/maaltijden/:pk/aanmelden/`, {
          aantal_gasten: gasten,
          gasten_eetwens: gasten_eetwens
        }, {params: {pk: pk}});
    },

    afmelden: (pk) => {
      return Q.xhr
        .post(`${api}/maaltijden/:pk/afmelden/`, {}, {params: {pk: pk}});
    },
  },

  mededelingen: {
    list: () => {
      return Q.xhr
        .get(`${api}/mededelingen/`);
    },

    get: (pk) => {
      return Q.xhr
        .get(`${api}/mededelingen/:pk/`, {params: {pk: pk}});
    }
  }
};

// make api available globally
window.api = api_obj;

module.exports = api_obj;
