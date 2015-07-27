let Reflux = require('reflux');
let api = require('api');

let actions = Reflux.createActions({
  // thread related actions
  load: {asyncResult: true},
  create: {asyncResult: true},
});

// Action async event handlers.
// They kick off the asynchronous action to the remote.
actions.load.listenAndPromise((pk, page) => api.forum.threads.list(pk, page));
actions.create.listenAndPromise(api.forum.threads.create);

module.exports = actions;
