import Reflux from 'reflux';
import api from 'api';
import _ from 'underscore';

let actions = Reflux.createActions({

  loadProfielen: {asyncResult: true},
  searchProfielen: {asyncResult: true},

  loadVerticale: {asyncResult: true},
  loadVerticalen: {asyncResult: true},

  loadCommissies : {asyncResult: true},

  loadKringen: {asyncResult: true}
});

actions.loadProfielen.listenAndPromise((page) => api.profiel.list(page));
actions.searchProfielen.listenAndPromise((search_text, filters) =>
                                         api.profiel.search(search_text, filters));
actions.loadVerticale.listenAndPromise((pk) => api.verticalen.get(pk));
actions.loadVerticalen.listenAndPromise(() => api.verticalen.list());

actions.loadCommissies.listenAndPromise((filter) => api.commissies.list(filter));

actions.loadKringen.listenAndPromise((filter) => api.kringen.list());

export default actions;
