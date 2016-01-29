import React from 'react';
import {
  Router,
  IndexRoute,
  Route,
  browserHistory,
  Link } from 'react-router';

// routing
import GroepenRouter from './Groepen';
import ForumRouter from "./Forum";
//import MededelingRouter from './Mededelingen';

// view components
import App from '../containers/App';
import Root from '../containers/Root';
import Login from "../containers/Login";
import NotFound from "../components/NotFound";

// <Route path="mededelingen">{MededelingRouter}</Route>
export default (
  <Route path="/" component={Root}>
    <IndexRoute component={NotFound} />
    <Route path="login" component={Login} />
    <Route path="leden">{GroepenRouter}</Route>
    <Route path="forum">{ForumRouter}</Route>
    <Route path="*" component={NotFound} />
  </Route>
);
