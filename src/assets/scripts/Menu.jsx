let React = require("react");
let Reflux = require('reflux');
let $ = require("jquery");
let _ = require("underscore");
let Grid = require("bootstrap");

import { Router, Route, IndexRoute, Link } from 'react-router';

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
    if(authStore.isAuthenticated()) {
      let user = authStore.getCurrentUser();
      return [
        <Link key="leden-link" to="leden">Leden</Link>,
        <Link key="mededelingen-link" to="mededelingen">Mededelingen</Link>,
        <Link key="profiel-link" to={`/leden/${user.pk}`}>Profiel</Link>
      ];
    } else {
      return [];
    }
  }

  render() {
    return (
      <div className="container">
        <div className="row">
          <Link to="/">Thuis</Link>
          { this.privateLinks() }
          <Link to="/forum">Reformaforum ({ this.state.forum_notifications })</Link>
        </div>
      </div>
    );
  }
}

module.exports = Menu;
