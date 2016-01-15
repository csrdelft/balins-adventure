import { arrayOf, normalize } from 'normalizr';
import { decamelize } from 'humps';
import * as meta from './meta';

/* E.g.:
 *   name: Profiel (camelcase!)
 *   schema: ShortProfiel (normalizr Schema of short profiel)
 *   getPromise: api.profiel.list (function of type pk -> promise([]))
 *
 * returns 3 action creaters:
 *   {
 *     requestList,
 *     receiveList,
 *     fetchList,
 *     loadList
 *   }
 */
export default function createListActions(name, schema, listPromise) {
  let REQ = 'REQUEST_' + (decamelize(name)).toUpperCase() + '_LIST';
  let REC = 'RECEIVE' + (decamelize(name)).toUpperCase() + '_LIST';

  let actions = {
    REQUEST : REQ,
    RECEIVE : REC,

    requestList: (extra_params={}) => {
      return {
        type: REQ,
        metatype: meta.REQUEST_ENTITIES,
        params: extra_params
      };
    },

    receiveList: (response, params={}) => {
      return {
        type: REC,
        metatype: meta.RECEIVE_ENTITIES,
        response: normalize(response, {data: arrayOf(schema)}),
        params: params
      };
    },

    fetchList: (extra_params={}) => {
      return dispatch => {
        dispatch(actions.requestList(extra_params));

        return listPromise()
          .catch((err) => console.error(err))
          .then(resp => {
            dispatch(
              actions.receiveList(resp, extra_params)
            );
          });
      };
    },

    loadList: (extra_params={}) => {
      return (dispatch) => {
        return dispatch(actions.fetchList(extra_params));
      };
    }
  };

  return actions;
}
