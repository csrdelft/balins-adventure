let React = require("react");
let Reflux = require('reflux');
let $ = require("jquery");
let _ = require("underscore");
let Grid = require("bootstrap");

let Router = require('react-router');
let { Route, DefaultRoute, Link, RouteHandler } = Router;

// data
let io = require('socket.io-client');
let { authStore } = require("auth/authStore");

// the top menu
// where we use the Link element from the router to activate different views
class Menu extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      forum_notifications: 0,
      user: undefined
    };

    this.socket = null;
  }

  componentWillMount() {
    // listen to auth changes
    // because the menu contents depends on auth state
    this.unsubscribe = authStore.listen((currentUser) => {
      this.setState({
        user: currentUser
      });
    });
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
    this.unsubscribe();
  }

  privateLinks() {
    return [
      <Link to="/groepen">Groepen</Link>,
      <Link to="/mededelingen">Mededelingen</Link>,
      <Link to="profiel-detail" params={{pk: 1337}}>Profiel</Link>
    ];
  }

  //TODO: uid to profiel should contain the uid of the current user
  render() {
    return (
      <div className="container">
        <div className="row">
          <Link to="/">Thuis</Link>
          { authStore.getCurrentUser() ? this.privateLinks() : false }
          <Link to="/forum">Reformaforum ({ this.state.forum_notifications })</Link>
        </div>
      </div>
    );
  }
}

module.exports = Menu;
