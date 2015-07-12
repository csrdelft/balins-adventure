var React = require('react');
var { Route, DefaultRoute } = require('react-router');

var MededelingList = require('./MededelingList');
var Mededeling = require('./Mededeling');
var MededelingListBeheer = require('./MededelingListBeheer');
var MededelingBeheer = require('./MededelingBeheer');

module.exports =
  <Route>
    <DefaultRoute name="mededeling-list" handler={MededelingList}/>
    <Route name="mededeling-beheer" path="beheer">
      <DefaultRoute handler={MededelingListBeheer}/>
      <Route name="mededeling-beheer-detail" path=":id" handler={MededelingBeheer}/>
    </Route>
    <Route name="mededeling-detail" path=":id" handler={Mededeling}/>
  </Route>;
