let _ = require('underscore');
let actions = require('./actions.js');
let Reflux = require('reflux');

let threadStore = Reflux.createStore({

  // listen to all forum action
  listenables: actions,

  init: function() {
    // thread store state
    this.threads = {};
  },

  onLoadCompleted: function(resp) {
    // handle load async completed action results
    // by replacing the store state
    this.threads = _.chain(resp.data)
      .map((thread) => [thread.pk, thread])
      .object()
      .value();

    this.trigger(this.threads);
  },

  onCreateCompleted: function(resp) {
    let thread = resp.data;
    this.threads[thread.pk] = thread;
    this.trigger(this.threads);
  }
});

module.exports = {
  threadStore: threadStore
};
