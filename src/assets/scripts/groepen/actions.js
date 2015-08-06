let Reflux = require('reflux');
let api = require('api');
let _ = require('underscore');

let actions = Reflux.createActions({

  // thread-list actions
  loadProfielen: {asyncResult: true},
  searchProfielen: {asyncResult: true}
});

actions.loadProfielen.listenAndPromise((page) => api.profiel.list(page));
actions.searchProfielen.listenAndPromise((search_text, filters) =>
                                         api.profiel.search(search_text, filters));

module.exports = actions;
