var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

var api = require("api");
var ForumThreadList = require("forum/ForumThreadList");
var PostForm = require("forum/PostForm");
var Profiel = require("partials/Profiel");
var io = require('socket.io-client');

var MededelingRouter = require('mededelingen/MededelingRouter');

var Router = require('react-router');
var {
  Route,
  DefaultRoute,
  Link,
  RouteHandler } = require('react-router');

// set the modern ui theme
var mui = require('material-ui');
var ThemeManager = new mui.Styles.ThemeManager();
ThemeManager.setTheme(ThemeManager.types.LIGHT);

// the top menu
// where we use the Link element from the router to activate different views
class Menu extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      forum_notifications: 0
    };

    this.socket = null;
  }

  componentDidMount() {
    // pick up notifications
    this.socket = io('http://localhost:3000/notifications');

    this.socket.on('connect', function() {
      console.log("Connected to notification server");
    });

    this.socket.on('message', function(msg) {
      console.log("Message:", msg);
    });

    this.socket.on('disconnect', function() {
      console.warn("Disconnected from notifications server");
    });
  }

  componentWillUnmount() {
    this.socket.close();
    this.socket = null;
  }

  render() {
    return (
      <ul>
        <li><Link to="/">Thuis</Link></li>
        <li><Link to="/groepen">Groepen</Link></li>
        <li>Actueel</li>
        <li><Link to="/forum">Reformaforum ({ this.state.forum_notifications })</Link></li>
        <li><Link to="/profiel/1337">Profiel</Link></li>
        <li><Link to="/mededelingen">Mededelingen</Link></li>
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

class Forum extends React.Component {
  render() {
    return (
      <div>
        <h1>Forum</h1>
        <ForumThreadList />
        <PostForm />
      </div>
    );
  }
}

// The actual routing tree.
// This binds client side routes to views
var routes = (
  <Route path="/" handler={App}>
    <Route path="" handler={NotFound} />
    <Route path="forum" handler={Forum} />
    <Route path="profiel/:uid" handler={Profiel} />
    <Route path="mededelingen">{MededelingRouter}</Route>
    <Route path="*" handler={NotFound} />
  </Route>
);

Router.run(routes, function (Handler, state) {
  React.render(<Handler params={state.params} />, $('#mount-app')[0]);
});
