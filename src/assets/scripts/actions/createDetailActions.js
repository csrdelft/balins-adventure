import { normalize } from 'normalizr';
import { decamelize } from 'humps';
import * as meta from './meta';

/* E.g.:
 *   name: Profiel (camelcase!)
 *   schema: Profiel (normalizr Schema of Profiel)
 *   getPromise: api.profiel.get (function of type pk -> promise)
 *
 * returns 3 action creaters:
 *   {
 *     request,
 *     receive,
 *     fetch,
 *     load
 *   }
 */
export default function createDetailActions(name, schema, getPromise) {
  let REQ = 'REQUEST_' + (decamelize(name)).toUpperCase() + '_DETAIL';
  let REC = 'RECEIVE_' + (decamelize(name)).toUpperCase() + '_DETAIL';

  let actions = {
    REQUEST : REQ,
    RECEIVE : REC,

    request: (pk, extra_params={}) => {
      return {
        type: REQ,
        metatype: meta.REQUEST_ENTITIES,
        params: Object.assign({}, extra_params, {pk: pk})
      };
    },

    receive: (response, params={}) => {
      return {
        type: REC,
        metatype: meta.RECEIVE_ENTITIES,
        response: normalize(response, {data: schema}),
        params: Object.assign({}, params)
      };
    },

    fetch: (pk, extra_params={}) => {
      return dispatch => {
        dispatch(actions['request'](pk, extra_params));
        return getPromise(pk)
          .catch((err) => console.error(err))
          .then(resp => {
            dispatch(
              actions['receive'](resp, Object.assign({pk: pk}, extra_params))
            );
          });
      };
    },

    load: (pk, extra_params={}) => {
      return (dispatch, getState) => {
        let { entities } = getState();
        let cache = entities[schema._key][pk];
        if(cache) {
          return null;
        } else {
          return dispatch(actions['fetch'](pk, extra_params));
        }
      };
    }
  };

  return actions;
}
