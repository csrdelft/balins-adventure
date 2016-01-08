import React from "react";
import $ from "jquery";
import { render } from 'react-dom';
import {
  Router,
  IndexRoute,
  Route,
  browserHistory,
  Link } from 'react-router';

// routing
import LedenRouter from 'groepen/LedenRouter';
import ForumRouter from "forum/Router";
import MededelingRouter from 'mededelingen/MededelingRouter';

// view components
import Login from "Login";
import NotFound from "NotFound";
import App from 'App';

// The actual routing tree.
// This binds client side routes to views
render(
  <Router history={browserHistory}>
    <Route path="/login" component={Login} />
    <Route path="/" component={App}>
      <IndexRoute component={NotFound} />
      <Route path="mededelingen">{MededelingRouter}</Route>
      <Route path="leden">{LedenRouter}</Route>
      <Route path="forum">{ForumRouter}</Route>
      <Route path="*" component={NotFound} />
    </Route>
  </Router>, $('#mount-app')[0]);

