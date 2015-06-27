var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

var api = require("api");
var ForumThreadList = require("partials/ForumThreadList");

var Router = require('react-router');
var {
  Route,
  DefaultRoute,
  Link,
  RouteHandler } = require('react-router');

// the menu
class Menu extends React.Component {
  render() {
    return (
      <ul>
        <li>
          <Link to="/">Thuis</Link>
        </li>
        <li>
          <Link to="/groepen">Groepen</Link>
        </li>
        <li>Actueel</li>
        <li>
          <Link to="/forum">Reformaforum</Link>
        </li>
      </ul>
    );
  }
}

lass App extends React.Component {
  render() {
    return <div>
      <div id="topmenu">
        <Menu />
      </div>
      <div id="content">
        <RouteHandler />
      </div>
    </div>;
  }
}

class NotFound extends React.Component {
  render() {
    return <div>
      <h1>Niks hier, behalve een 404</h1>
    </div>;
  }
}

// the router
var routes = (
  <Route path="/" handler={App}>
    <Route path="" handler={NotFound} />
    <Route path="forum" handler={ForumThreadList} />
    <Route path="*" handler={NotFound} />
  </Route>
);


Router.run(routes, function (Handler) {
  React.render(<Handler />, $('#mount-app')[0]);
});
