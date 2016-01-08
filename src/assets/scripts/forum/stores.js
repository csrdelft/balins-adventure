import _ from 'underscore';
import actions from './actions.js';
import Reflux from 'reflux';

// Store that specializes in paginated thread lists
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
      let page = forum[1] || [];
      page[thread.pk] = thread;
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
    );
  }
});

// paginated detail store for threads
let threadDetailStore = Reflux.createStore({

  // listen to all forum action
  listenables: actions,

  init: function() {
    // threadpk -> [ page -> posts ]
    this.threads = {};
  },

  updateThread: function(thread) {
    // order posts by page
    let posts_page = _.clone(thread.posts);
    thread.posts = (this.threads[thread.pk] || {posts: {}}).posts;
    thread.posts[posts_page.pageno] = posts_page;

    // update the state
    this.threads[thread.pk] = thread;
    this.threads[thread.pk].last_page = posts_page.last_page;

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
    delete this.threads[resp.config.params.pk];
  },

  onCreatePostCompleted: function(resp) {
    let post = resp.data;
    let thread = this.threads[post.draad];

    // newest posts are on the last page
    let page = _.max(thread.posts, (_, pageno) => pageno);

    // if the thread or posts page is not in the store, no one is interested
    if(thread !== undefined && page !== undefined) {
      // reload that page of this thread
      // this will eventually kick the listeners
      actions.loadThread(thread.pk, page.pageno);
    }
  },

  onDeletePostCompleted: function(resp) {
    // we don't have enough information from the delete
    // to reload (missing the page of the post)
  }
});

module.exports = {
  threadListStore: threadListStore,
  threadDetailStore: threadDetailStore
};
