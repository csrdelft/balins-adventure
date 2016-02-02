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
import AgendaRouter from "./Agenda";
import MededelingenRouter from './Mededelingen';

// view components
import App from '../containers/App';
import Root from '../containers/Root';
import Login from "../containers/Login";
import NotFound from "../components/NotFound";

export default (
  <Route path="/" component={Root}>
    <IndexRoute component={NotFound} />
    <Route path="login" component={Login} />
    <Route path="leden">{GroepenRouter}</Route>
    <Route path="agenda">{AgendaRouter}</Route>
    <Route path="forum">{ForumRouter}</Route>
    <Route path="mededelingen">{MededelingenRouter}</Route>
    <Route path="*" component={NotFound} />
  </Route>
);
