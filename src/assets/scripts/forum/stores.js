let _ = require('underscore');
let actions = require('./actions.js');
let Reflux = require('reflux');

// Store that specializes in paginated thread lists
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

// Store that specializes in threads by pk
// Updates from this store are a Map[pk -> thread]
// Each thread has a field 'posts' that is a Map[page -> posts_page]
let threadStore = Reflux.createStore({

  // listen to all forum action
  listenables: actions,

  init: function() {
    // thread store state
    this.threads = {};
  },

  updateThread: function(thread) {
    // order posts by page
    let posts_page = _.clone(thread.posts);
    thread.posts = (this.threads[thread.pk] || {posts: {}}).posts;
    thread.posts[posts_page.pageno] = posts_page;

    // update the state
    this.threads[thread.pk] = thread;

    this.trigger(this.threads);
  },

  //
  // Handlers
  //

  onCreateThreadCompleted: function(resp) {
    this.updateThread(resp.data);
  },

  onLoadThreadCompleted: function(resp) {
    this.updateThread(resp.data);
  },

  onCreatePostCompleted: function(resp) {
    let post = resp.data;
    let thread = this.threads[post.draad];

    // newest posts are on the last page
    let page = _.max(thread.posts, (_, pageno) => pageno);

    // if the thread or posts page is not in the store, no one is interested
    if(thread !== undefined && page !== undefined) {
      // optimistic update
      page.results.unshift(post);

      // reload the first page of this thread
      actions.loadThread(thread.pk, 1);

      // notify listeners
      this.trigger(this.threads);
    }
  }
});

module.exports = {
  threadsByPageStore: threadsByPageStore,
  threadStore: threadStore
};
