var React = require('react');
var { Route, DefaultRoute } = require('react-router');

var Profiel = require('./Profiel');
var ProfielList = require('./ProfielList');
var ProfielLink = require('./ProfielLink.jsx');

module.exports =
	<Route>
		<Route name='profiel-detail' path=":pk" handler={Profiel}/>
    <Route name='profiel-list' path="overzicht/:page" handler={ProfielList}/>
	</Route>;
