import React from "react";
import $ from "jquery";
import _ from "underscore";
import { render } from 'react-dom';
import { syncHistory, routeReducer } from 'react-router-redux';
import { combineReducers } from 'redux';
import * as immutable from 'immutable';
import * as meta from 'actions/meta';
import * as actions from 'actions';
import { ShortProfiel } from 'actions/profiel';
import { normalize, arrayOf } from 'normalizr';
import { parse } from 'json3';

// useful for debuggin'
window._ = _;
window.$ = $;
window.immutable = immutable;

import configureStore from 'store/configureStore';
import history from 'store/history';

import App from 'containers/App';
import * as reducers from 'reducers';

// load the preloaded data from the dom into the initial store state
let initialState = {};

let reducer = combineReducers(Object.assign({}, reducers, {routing: routeReducer}));
let store = configureStore(reducer, initialState);

// call actions to handle preload data
let preloadData = parse(window.preloadData);
store.dispatch({
  metatype: meta.RECEIVE_ENTITIES,
  response: normalize(preloadData, {user: ShortProfiel})
});
if(preloadData.user) {
  store.dispatch(actions.auth.preloadLogin(preloadData.user));
}

render(<App store={store} history={history} /> , $('#mount-app')[0]);

