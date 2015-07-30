let Reflux = require('reflux');
let api = require('api');
let _ = require('underscore');

let actions = Reflux.createActions({

  // thread-list actions
  loadThreads: {asyncResult: true}, // load thread list (page, forum_pk)

  // single thread actions
  loadThread: {asyncResult: true},  // load single thread (thread_pk)
  createThread: {asyncResult: true},
  deleteThread: {asyncResult: true},

  createPost: {asyncResult: true},

});

//
// arguments to api repeated here for clarity
//

// thread related
actions.loadThreads
  .listenAndPromise((pk, page) => api.forum.threads.list(pk, page));
actions.loadThread
  .listenAndPromise((pk, postsPage) => api.forum.threads.get(pk, postsPage));
actions.createThread
  .listenAndPromise((thread) => api.forum.threads.create(thread));
actions.deleteThread
  .listenAndPromise((thread_pk) => api.forum.threads.delete(thread_pk));

// post related
actions.createPost.listenAndPromise((post) => api.forum.posts.create(post));

module.exports = actions;
