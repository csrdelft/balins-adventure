let Reflux = require('reflux');
let api = require('api');
let _ = require('underscore');

let actions = Reflux.createActions({

  loadProfielen: {asyncResult: true},
  searchProfielen: {asyncResult: true},

  loadVerticale: {asyncResult: true},
  loadVerticalen: {asyncResult: true}
});

actions.loadProfielen.listenAndPromise((page) => api.profiel.list(page));
actions.searchProfielen.listenAndPromise((search_text, filters) =>
                                         api.profiel.search(search_text, filters));
actions.loadVerticale.listenAndPromise((pk) => api.verticalen.get(pk));
actions.loadVerticalen.listenAndPromise(() => api.verticalen.list());

module.exports = actions;
