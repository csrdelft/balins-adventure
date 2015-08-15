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
    this.verticalen= [];
  },

  // getters

  getAll: function() { return this.verticalen; },

  // handlers

  onLoadVerticalenCompleted: function(resp) {
    this.verticalen = resp.data;
    this.trigger(this.verticalen);
  }
});

let verticaleDetailStore = Reflux.createStore({
  listenables : actions,

  init: function() {
    this.verticalen = {};
  },

  // getters

  get: function(pk) { return this.verticalen[pk]; },

  // handlers

  onLoadVerticaleCompleted: function(resp) {
    this.verticalen[resp.data.pk] = resp.data;
    this.trigger(this.verticalen);
  }
});

let kringListStore = Reflux.createStore({
  listenables : actions,

  init: function() {
    this.kringen = [];
  },

  // getters

  getAll: function() { return this.kringen; },

  getVerticaleChoices: function() {
    return _.chain(this.kringen).map((k) => k.verticale).uniq().value();
  },

  getFamilieChoices: function() {
    return _.chain(this.kringen).map((k) => k.familie).uniq().value();
  },

  // handlers

  onLoadKringenCompleted: function(resp) {
    this.kringen = resp.data;
    this.trigger(this.kringen);
  }
});

module.exports = {
  profielListStore: profielListStore,
  verticaleListStore: verticaleListStore,
  verticaleDetailStore: verticaleDetailStore,
  kringListStore: kringListStore
};
