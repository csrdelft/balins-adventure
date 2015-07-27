let React = require("react");
let Reflux = require('reflux');
let $ = require("jquery");
let _ = require("underscore");
let Grid = require("bootstrap");

let api = require("api");
let ForumRouter = require("forum/Router");
let MededelingRouter = require('mededelingen/MededelingRouter');

let Router = require('react-router');
let { Route, DefaultRoute, Link, RouteHandler } = Router;
let io = require('socket.io-client');

let ProfielRouter = require('groepen/ProfielRouter');

let forms = require('forms');
let mui = require('material-ui');

// configure mui
let ThemeManager = new mui.Styles.ThemeManager();
ThemeManager.setTheme(ThemeManager.types.LIGHT);

// configure reflux
Reflux.setPromiseFactory(require('q').Promise);

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

  //TODO: uid to profiel should contain the uid of the current user
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

  static get childContextTypes() {
    return { muiTheme: React.PropTypes.object }
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

class Login extends React.Component {

  static get contextTypes() {
    return { router: React.PropTypes.object.isRequired }
  }

  static get childContextTypes() {
    return { muiTheme: React.PropTypes.object }
  }

  getChildContext() {
    return {
      // set the mui theme on the children through the context
      muiTheme: ThemeManager.getCurrentTheme()
    };
  }

  constructor(props) {
    super(props);

    this.state = {
      error_text: ""
    };
  }

  setError(text) {
    this.setState({
      error_text: text
    });
  }

  submit(data) {
    api.login(data)
      .then(
        (resp) => {
          console.debug(`Now logged in as ${resp.data.full_name}`);

          this.context.router.transitionTo("/");
        },
        (resp) => this.setError(resp.data.detail)
      );
  }

  render() {
    let formBuilder = () => {
      return (
        <Grid.Col id="login" offsetSm={4} sm={4}>
          <Grid.Row id="login-header">
            <h1>Inloggen</h1>
          </Grid.Row>
          {
            this.state.error_text
              ? <p>{this.state.error_text}</p>
              : false
          }
          <forms.CharField name="username" label="Gebruikersnaam" />
          <forms.PasswordField name="password" label="Wachtwoord" />

          <Grid.Row id="login-footer">
            <forms.SubmitButton />
          </Grid.Row>
        </Grid.Col>
      );
    }

    return (
      <Grid.Container>
        <Grid.Row>
          <forms.Form ref="form"
            formBuilder={formBuilder}
            onSubmit={this.submit.bind(this)} />
        </Grid.Row>
      </Grid.Container>
    );
  }
}

// The actual routing tree.
// This binds client side routes to views
let routes = (
  <Route>
    <Route path="/login" handler={Login} name="login" />
    <Route path="/" handler={App}>
      <DefaultRoute handler={NotFound} />
      <Route path="forum">{ForumRouter}</Route>
      <Route path="mededelingen">{MededelingRouter}</Route>
      <Route path="profiel">{ProfielRouter}</Route>
      <Route path="*" handler={NotFound} />
    </Route>
  </Route>
);

Router.run(routes, function (Handler, state) {
  React.render(<Handler {...state.params} />, $('#mount-app')[0]);
});
