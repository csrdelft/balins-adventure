let _ = require('underscore');
let actions = require('./actions.js');
let Reflux = require('reflux');

let profielListStore = Reflux.createStore({
  listenables : actions,

  init: function() {
    // Map[pageno -> [profiel]]
    this.profielen = {};
  },

  // getters

  getAll: function() { return this.profielen; },

  // handlers

  onLoadProfielenCompleted: function(resp) {
    let page = resp.data.pageno;
    let profielen_page = resp.data.results;

    this.profielen[page] = profielen_page;
    this.trigger(this.profielen);
  }
});

let verticaleListStore = Reflux.createStore({
  listenables : actions,

  init: function() {
    this.verticalen= {};
  },

  // getters

  getAll: function() { return this.verticalen; },

  // handlers

  onLoadVerticalenCompleted: function(resp) {
    this.verticalen = resp.data;
    this.trigger(this.verticalen);
  }
});

module.exports = {
  profielListStore: profielListStore,
  verticaleListStore: verticaleListStore
};
