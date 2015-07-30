let _ = require('underscore');
let actions = require('./actions.js');
let Reflux = require('reflux');

// Store that specializes in paginated thread lists
// updates from this store are tuples [ page, threads ]
let threadListStore = Reflux.createStore({

  // listen to all forum action
  listenables: actions,

  init: function() {
    // Map[forum -> Map[page -> Map[pk -> thread]]]
    this.threads = {};
  },

  //
  // getters
  // (they won't perform actions, so if something is not in the store,
  // you'll have to query the right actions yourself)
  //

  // returns undefined when the data is not in the store
  getForumPage: function(forum_pk, page) {
    let forum = this.threads[forum_pk];
    if(forum)
      return forum[page];
    else
      return undefined;
  },


  //
  // Handlers
  //

  onLoadThreadsCompleted: function(resp) {
    // handle load async completed action results
    // by replacing the store state
    let threads = resp.data.results;
    let forum_pk = resp.config.params.forum;

    let forum = this.threads[forum_pk] || {};

    // transform the thread list into a Map[pk -> thread]
    forum[resp.data.pageno] = _
      .chain(threads)
      .map((thread) => [thread.pk, thread])
      .object()
      .value();

    this.threads[forum_pk] = forum;

    this.trigger(this.threads);
  },

  onCreateThreadCompleted: function(resp) {
    let thread = resp.data;

    // get the right forum
    let forum = this.threads[thread.forum];

    // ignore if the forum part is not loaded
    if(forum) {
      // add the new thread to the front of the first page
      let page = this.threadsByPage[1] || [];
      page.unshift(resp.data);
      forum[1] = page;
      this.trigger(this.threads);
    }
  },

  onDeleteThreadCompleted: function(resp) {
    let thread_pk = resp.config.params.pk;

    // search for the thread in the store
    _(this.threads).each((forum) =>
      _(forum).each((threadsByPage) => {
        // delete the thread from the store
        // and notify observers
        if(threadsByPage[thread_pk]) {
          delete threadsByPage[thread_pk];
          this.trigger(this.threads);
        }
      })
    )

  },
});

// Store that specializes in threads by pk
// Updates from this store are a Map[pk -> thread]
// Each thread has a field 'posts' that is a Map[page -> posts_page]
let threadDetailStore = Reflux.createStore({

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

  onDeleteThreadCompleted: function(resp) {
    delete this.threads[resp.req_data.pk];
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
  threadListStore: threadListStore,
  threadDetailStore: threadDetailStore
};
