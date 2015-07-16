let React = require('react');
let { Route, DefaultRoute } = require('react-router');

let Mededelingen = require('./Mededelingen');
let MededelingDetail = require('./MededelingDetail');

module.exports = <Route handler={Mededelingen}>
  <Route path=":pk" name="mededeling-detail" handler={MededelingDetail} />
</Route>;
