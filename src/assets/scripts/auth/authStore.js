let _ = require('underscore');
let actions = require('./actions.js');
let Reflux = require('reflux');

let authStore = Reflux.createStore({

  listenables: actions,

  init: function() {
    this.user = undefined;
  },

  update: function(user) {
    if(user && user.pk) {
      this.authenticated = true;
      this.user = user;
    } else {
      this.authenticated = false;
      this.user = undefined;
    }

    // notify listeners
    this.trigger(this.user);
  },

  //
  // getters
  //

  getCurrentUser: function() {
    return this.user;
  },

  //
  // handlers
  //

  onLoginCompleted: function(resp) {
    this.update(resp.data);
  },

  onLoadCurrentCompleted: function(user) {
    this.update(user);
  }

});

module.exports = {
  authStore: authStore
}
