let _ = require('underscore');
let actions = require('./actions.js');
let Reflux = require('reflux');

let profielListStore = Reflux.createStore({
  listenables : actions,

  init: function() {
    // Map[pageno -> [profiel]]
    this.profielen = {};
  },

  onLoadProfielenCompleted: function(resp) {
    let page = resp.data.pageno;
    let profielen_page = resp.data.results;

    this.profielen[page] = profielen_page;
    this.trigger(this.profielen);
  }
});

module.exports = {
  profielListStore: profielListStore
};
