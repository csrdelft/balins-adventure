import initialState from '../store';
import * as actions from '../actions';
import {Map} from 'immutable';
import _ from 'underscore';
import {merge} from 'lodash/object';

export function entities(state = {
    profielen: {},
    shortProfielen: {},
    kringen: {},
    commissies: {},
    onderverenigingen: {},
    verticalen: {},
    overigeGroepen: {},
    werkgroepen: {}
  }, action) {
  if(action.response && action.response.entities) {
    console.log(merge({}, state, action.response.entities));
    return merge({}, state, action.response.entities);
  }

  return state;
};

export function shortProfielenByFilter(state=Map(), action) {
  switch(action.type) {
    case actions.RECEIVE_PROFIEL_LIST:
      let { filter, response: {entities} } = action;
      return state.set(filter, _.keys(entities.shortProfielen));
    default:
      return state;
  };
};
