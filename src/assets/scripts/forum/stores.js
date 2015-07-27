let _ = require('underscore');
let actions = require('./actions.js');
let Reflux = require('reflux');

// updates from this store are tuples [ page, threads ]
let threadsByPageStore = Reflux.createStore({

  // listen to all forum action
  listenables: actions,

  init: function() {
    // Map[page -> [thread]]
    this.threadsByPage = {};
  },

  //
  // Handlers
  //

  onLoadThreadsCompleted: function(resp) {
    // handle load async completed action results
    // by replacing the store state
    let threads = resp.data.results;
    this.threadsByPage[resp.config.params.page] = threads;
    this.trigger([resp.config.params.page, threads]);
  },

  onCreateThreadCompleted: function(resp) {
    // add the new thread to the front of the first page
    let page = this.threadsByPage[1] || [];
    page.unshift(resp.data);
    this.threadsByPage[1] = page;

    this.trigger([1, this.threads]);
  },
});

// updates from this store is a Map[pk -> thread]
let threadStore = Reflux.createStore({

  // listen to all forum action
  listenables: actions,

  init: function() {
    // thread store state
    this.threads = {};
  },

  updateThread: function(thread) {
    this.threads[thread.pk] = thread;
    this.trigger(this.threads);
  },

  //
  // Handlers
  //

  onCreateThreadCompleted: function(resp) {
    this.updateThread(resp.data);
  },

  onLoadThreadsCompleted: function(resp) {
    this.threads = _
      .chain(resp.data)
      .map((thread) => [thread.pk, thread])
      .object()
      .value();

    this.trigger(this.threads);
  },

  onLoadThreadCompleted: function(resp) {
    this.updateThread(resp.data);
  },

  onCreatePostCompleted: function(resp) {
    let post = resp.data;
    let thread = this.threads[post.draad];

    // if the thread is not in the store, no one is interested
    if(thread !== undefined) {
      // optimistic update
      thread.posts.push(post);

      // reload the single thread
      actions.loadThread(thread.pk);

      // notify listeners
      this.trigger(this.threads);
    }
  }
});

module.exports = {
  threadsByPageStore: threadsByPageStore,
  threadStore: threadStore
};
