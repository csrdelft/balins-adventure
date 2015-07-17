let React = require("react");
let $ = require("jquery");
let _ = require("underscore");

var api = require("api");
var ForumThreadList = require("forum/ForumThreadList");
var PostForm = require("forum/PostForm");
var ProfielLink = require("groepen/ProfielLink");

var ProfielRouter = require('groepen/ProfielRouter');
let Profiel = require("groepen/Profiel");
let ForumRouter = require("forum/Router");
let MededelingRouter = require('mededelingen/MededelingRouter');

let Router = require('react-router');
let { Route, DefaultRoute, Link, RouteHandler } = require('react-router');

// sockets yeah
let io = require('socket.io-client');

// set the modern ui theme
let mui = require('material-ui');
let ThemeManager = new mui.Styles.ThemeManager();
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
      <div className="container">
        <div className="row">
          <Link to="/">Thuis</Link>
          <Link to="/groepen">Groepen</Link>
          <Link to="/mededelingen">Mededelingen</Link>
          <Link to="profiel-detail" params={{pk: 1337}}>Profiel</Link>
          <Link to="/forum">Reformaforum ({ this.state.forum_notifications })</Link>
        </div>
      </div>
    );
  }
}

// the top level application just wraps the router.
// The router is in charge of rendering the right child view based on the url.
class App extends React.Component {
  render() {
    return (
      <div>
        <div id="global-nav">
          <Menu />
        </div>

        <div id="app">
          <div id="app-header-fill">
          </div>

          <div className="container-fluid">
            <RouteHandler {...this.props} />
          </div>
        </div>
      </div>
    );
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
let routes = (
  <Route path="/" handler={App}>
    <Route path="" handler={NotFound} />
    <Route path="forum">{ForumRouter}</Route>
    <Route path="mededelingen">{MededelingRouter}</Route>
    <Route path="profiel">{ProfielRouter}</Route>
    <Route path="*" handler={NotFound} />
  </Route>
);

Router.run(routes, function (Handler, state) {
  React.render(<Handler {...state.params} />, $('#mount-app')[0]);
});
