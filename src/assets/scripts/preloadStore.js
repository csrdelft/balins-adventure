let _ = require('underscore');
let Reflux = require('reflux');

// some data can be pushed from the server on page load,
// because we need it always anyways.
// This store keeps track of that data.
// The store is only filled with data on page load, and then stable,
// so don't expect data in here to be up-to-date.
let preloadStore = Reflux.createStore({

  init: function() {
    // default the global preload data object
    if(window.preloadData === undefined) {
      window.preloadData = {
        user: undefined,
      };
    }
  },

  get: function(name) {
    return window.preloadData[name];
  },


  //
  // convenience getters
  //

  getCurrentUser: function() { return this.get('user'); },
});

module.exports = preloadStore;
