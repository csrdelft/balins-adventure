let React = require("react");
let Reflux = require('reflux');
let $ = require("jquery");
let _ = require("underscore");
let Grid = require("bootstrap");

// routing
let Router = require('react-router');
let { Route, DefaultRoute, Link, RouteHandler } = Router;
let ProfielRouter = require('groepen/ProfielRouter');
let ForumRouter = require("forum/Router");
let MededelingRouter = require('mededelingen/MededelingRouter');

// ui
let mui = require('material-ui');
let ThemeManager = new mui.Styles.ThemeManager();
ThemeManager.setTheme(ThemeManager.types.LIGHT);

// view components
let Login = require("Login");
let Menu = require("Menu");

// data
let authActions = require("auth/actions");
let authStore = require("auth/authStore");

// configure reflux
Reflux.setPromiseFactory(require('q').Promise);

// the top level application just wraps the router.
// The router is in charge of rendering the right child view based on the url.
class App extends React.Component {

  static get childContextTypes() {
    return { muiTheme: React.PropTypes.object }
  }

  componentWillMount() {
    //
    // here we can globally initialize some data loading
    // by kicking of a bunch of actions
    //

    // make sure current user data is loaded
    authActions.loadCurrent();
  }

  getChildContext() {
    return {
      // set the mui theme on the children through the context
      muiTheme: ThemeManager.getCurrentTheme()
    };
  }

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
  <Route>
    <Route path="/login" handler={Login} name="login" />
    <Route path="/" handler={App}>
      <DefaultRoute handler={NotFound} />
      <Route path="mededelingen">{MededelingRouter}</Route>
      <Route path="profiel">{ProfielRouter}</Route>
      <Route path="forum">{ForumRouter}</Route>
      <Route path="*" handler={NotFound} />
    </Route>
  </Route>
);

Router.run(routes, function (Handler, state) {
  React.render(<Handler {...state.params} />, $('#mount-app')[0]);
});
