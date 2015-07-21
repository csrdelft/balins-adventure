var React = require('react');
var { Route, DefaultRoute } = require('react-router');

var Profiel = require('./Profiel');
var ProfielLink = require('./ProfielLink.jsx');

module.exports =
	<Route>
		<Route name='profiel-detail' path=":pk" handler={Profiel}/>
	</Route>;
