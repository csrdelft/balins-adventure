var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

var api = require("api");
var ForumThreadList = require("partials/ForumThreadList");
var Profiel = require("partials/Profiel");

var Router = require('react-router');
var {
  Route,
  DefaultRoute,
  Link,
  RouteHandler } = require('react-router');

// the top menu
// where we use the Link element from the router to activate different views
class Menu extends React.Component {
  render() {
    return (
      <ul>
        <li><Link to="/">Thuis</Link></li>
        <li><Link to="/groepen">Groepen</Link></li>
        <li>Actueel</li>
        <li><Link to="/forum">Reformaforum</Link></li>
        <li><Link to="/profiel/1337">Profiel</Link></li>
      </ul>
    );
  }
}

// the top level application just wraps the router.
// The router is in charge of rendering the right child view based on the url.
class App extends React.Component {
  render() {
    return <div>
      <div id="topmenu"><Menu /></div>
      <div id="content"><RouteHandler {...this.props} /></div>
    </div>;
  }
}

// simple 404 child view
class NotFound extends React.Component {
  render() {
    return <div>
      <h1>Niks hier, behalve een 404</h1>
    </div>;
  }
}

// The actual routing tree.
// This binds client side routes to views
var routes = (
  <Route path="/" handler={App}>
    <Route path="" handler={NotFound} />
    <Route path="forum" handler={ForumThreadList} />
    <Route path="profiel/:uid" handler={Profiel} />
    <Route path="*" handler={NotFound} />
  </Route>
);


Router.run(routes, function (Handler, state) {
  React.render(<Handler params={state.params} />, $('#mount-app')[0]);
});
