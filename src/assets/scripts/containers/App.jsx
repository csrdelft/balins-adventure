import React, {Component, PropTypes} from "react";
import {Provider} from 'react-redux';
import {Router, browserHistory} from 'react-router';
import $ from "jquery";
import _ from "underscore";
import DevDock from "./DevDock";

import routes from '../routes';

// the top level application just wraps the router.
// The router is in charge of rendering the right child view based on the url.
export default class App extends Component {

  static get propTypes() {
    return {
      store: PropTypes.object.isRequired,
      history: PropTypes.object.isRequired
    };
  }

  componentWillMount() {
    //
    // here we can globally initialize some data loading
    // by kicking of a bunch of actions
    //

    // make sure current user data is loaded
    // authActions.loadCurrent();
  }

  render() {
    let { store, history } = this.props;

    return (
      <Provider store={store}>
        <div>
          <Router history={history}>
            {routes}
          </Router>
          <DevDock />
        </div>
      </Provider>
    );
  }
}
