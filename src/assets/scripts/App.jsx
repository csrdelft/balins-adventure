import React from "react";
import Reflux from 'reflux';
import $ from "jquery";
import _ from "underscore";
import Grid from "bootstrap";
import Layout from 'Layout';
import { IndexRoute, Route, Link } from 'react-router';

// view components
import Menu from "Menu";

// data
import authActions from "auth/actions";

// configure reflux
Reflux.setPromiseFactory(require('q').Promise);

// the top level application just wraps the router.
// The router is in charge of rendering the right child view based on the url.
export default class App extends React.Component {

  componentWillMount() {
    //
    // here we can globally initialize some data loading
    // by kicking of a bunch of actions
    //

    // make sure current user data is loaded
    authActions.loadCurrent();
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
            {this.props.children}
          </div>
        </div>
      </div>
    );
  }
}
