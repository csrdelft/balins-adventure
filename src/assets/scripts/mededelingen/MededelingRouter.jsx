var React = require('react');
var { Route, DefaultRoute } = require('react-router');

var MededelingList = require('./MededelingList');
var Mededeling = require('./Mededeling');

module.exports =
  <Route>
    <DefaultRoute name="mededeling-list" handler={MededelingList}/>
    <Route name="mededeling-detail" path=":id" handler={Mededeling}/>
  </Route>;
