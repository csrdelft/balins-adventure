let Reflux = require('reflux');
let api = require('api');

let actions = Reflux.createActions({

  loadThreads: {asyncResult: true}, // load thread list (page, forum_pk)
  loadThread: {asyncResult: true},  // load single thread (thread_pk)
  createThread: {asyncResult: true},

  createPost: {asyncResult: true},

});

//
// arguments to api repeated here for clarity
//

// thread related
actions.loadThreads.listenAndPromise((pk, page) => api.forum.threads.list(pk, page));
actions.loadThread.listenAndPromise((pk, postsPage) => api.forum.threads.get(pk, postsPage));
actions.createThread.listenAndPromise((thread) => api.forum.threads.create(thread));

// post related
actions.createPost.listenAndPromise((post) => api.forum.posts.create(post));

module.exports = actions;
