var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

var api = require("api");
var ForumThreadList = require("partials/ForumThreadList");

var HashHistory = require('react-router/lib/HashHistory');
var { Router, Route, DefaultRoute, Link } = require('react-router');

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

class App extends React.Component {
  render() {
    return <div>
      <div id="topmenu">
        <Menu />
      </div>
      <div id="content">
        { this.props.children ? this.props.children : <div><h1>Hi!</h1></div> }
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
var app = <Router history={new HashHistory}>
  <Route path="/" component={App}>
    <Route path="forum" component={ForumThreadList} />
    <Route path="*" component={NotFound} />
  </Route>
</Router>;

React.render(app, $('#mount-app')[0]);
