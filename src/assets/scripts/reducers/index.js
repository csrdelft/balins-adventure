import * as actions from '../actions';
import {Map, fromJS} from 'immutable';
import _ from 'underscore';
import {merge} from 'lodash/object';
import * as meta from '../actions/meta';

export function entities(state = {
    profielen: {},
    shortProfielen: {},
    kringen: {},
    commissies: {},
    onderverenigingen: {},
    verticalen: {},
    overigeGroepen: {},
    werkgroepen: {},
    posts: {},
    draadjes: {},
    forums: {}
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

export function shortProfielenByFilter(state=Map(), action) {
  switch(action.type) {
    case (actions.RECEIVE_PROFIEL_LIST):
      let { filter, response: {entities} } = action;
      // paginage by filter
      // gotta use immutable JS Maps instead of plain JS objects,
      // because only the former has value semantics
      return state.set(fromJS(filter), _.keys(entities.shortProfielen));

    default:
      return state;
  };
};

export function postsByThreadParams(state=Map(), action) {
  switch(action.type) {
    case (actions.forumDraad.RECEIVE):
      // paginate by thread pk & page
      return state.set(fromJS(action.params), _(action.response.entities.posts).keys());

    default:
      return state;
  };
};
