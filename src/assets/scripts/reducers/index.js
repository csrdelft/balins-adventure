import * as actions from '../actions';
import {Map, fromJS} from 'immutable';
import _ from 'underscore';
import {merge} from 'lodash/object';
import * as meta from '../actions/meta';
import { normalize } from 'normalizr';

export function entities(state = {
    profielen: {},
    shortProfielen: {},
    kringen: {},
    commissies: {},
    onderverenigingen: {},
    shortVerticalen: {},
    verticalen: {},
    overigeGroepen: {},
    werkgroepen: {},
    posts: {},
    draadjes: {},
    shortDraadjes: {},
    forums: {},
    mededelingen: {}
  }, action) {

  switch(action.metatype) {
    
    case (meta.RECEIVE_ENTITIES):

      // recursively merge the entities in the store
      return merge({}, state, action.response.entities);

    case (meta.RECEIVE_DELETE_ENTITY):

      // We use a soft delete because the entity might be mentioned by other entities
      // through foreign keys; this way the UI/selector is responsible for filtering out
      // soft deleted items, but at least we don't get unexpected undefineds
      let {entityType, pk} = action;
      return merge({}, state, {
        [entityType]: {
          [action.pk]: Object.assign({}, state[entityType][pk], {_isDeleted: true})
        }
      });

    default:
      return state;
  }

  return state;
};

export function shortProfielenByParams(state=Map(), action) {
  switch(action.type) {
    case (actions.RECEIVE_PROFIEL_LIST):
      let { params, response: {entities} } = action;

      // paginage by params
      // gotta use immutable JS Maps instead of plain JS objects,
      // because only the former has value semantics
      return state.set(fromJS(params), _.keys(entities.shortProfielen));

    default:
      return state;
  };
};

export function shortDraadjesByParams(state=Map(), action) {
  switch(action.type) {
    case (actions.forumDraad.RECEIVE_LIST):
    
      let { params, response: {entities} } = action;
      return state.set(fromJS(params), _.keys(entities.shortDraadjes));

    default:
      return state;
  }
}

export function postsByThreadParams(state=Map(), action) {
  switch(action.type) {
    case (actions.forumDraad.RECEIVE):
      // paginate posts by thread pk & page
      return state.set(fromJS(action.params), _(action.response.entities.posts).keys());

    default:
      return state;
  };
};

export function auth(state={currentUser: null}, action) {
  switch(action.type) {
    case (actions.auth.LOGIN_SUCCESS):
      return Object.assign({}, state, {
        currentUser: action.response.result.data
      });

    case (actions.auth.PRELOAD_LOGIN_SUCCESS):
      return Object.assign({}, state, {
        currentUser: action.user.pk
      });

    default:
      return state;
  }
};
