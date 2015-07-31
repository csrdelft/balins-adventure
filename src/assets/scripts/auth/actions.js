let Reflux = require('reflux');
let api = require('api');
let _ = require('underscore');
let preloadStore = require("preloadStore");
let Q = require("q");

let actions = Reflux.createActions({

  loadCurrent: {asyncResult: true},
  login: {asyncResult: true},

});

// load will try to fetch the current user data from the
// preload store, if not available, it will ask the server for the current user
actions.loadCurrent.listenAndPromise(() => {
  let preloadUser = preloadStore.getCurrentUser()
  if(preloadUser) {
    // fake a succesful api call
    return Q.fcall(() => preloaduser);
  } else {
    // make an actual api call to determine the user
    return api.auth.get().then((resp) => resp.data);
  }
});

// kick of async actions
actions.login.listenAndPromise((user, pw) => api.auth.login(user, pw));

module.exports = actions;

