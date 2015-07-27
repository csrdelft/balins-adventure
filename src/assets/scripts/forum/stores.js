let _ = require('underscore');
let actions = require('./actions.js');
let Reflux = require('reflux');

let threadStore = Reflux.createStore({
  listenables: actions,

  init: function() {
    this.threads = {};
  },

  onLoadCompleted: function(resp) {
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
