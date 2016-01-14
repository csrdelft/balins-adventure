import api from '../utils/api';
import { normalize, Schema, arrayOf } from 'normalizr';
import createDetailActions from './createDetailActions';
import * as meta from './meta';

// Action types:
// Used to identify the action uniquely from the listeners (i.e. reducers)
export const RECEIVE_PROFIEL = 'RECEIVE_PROFIEL';
export const REQUEST_PROFIEL = 'REQUEST_PROFIEL';
export const RECEIVE_PROFIEL_LIST = 'RECEIVE_PROFIEL_LIST';
export const REQUEST_PROFIEL_LIST = 'REQUEST_PROFIEL_LIST';

// Schemas
// Describe the JSON structure that we get back from the API.
// Primarily used to normalize the nested reponses into a flat structure using normalizr
const Profiel = new Schema('profielen', {idAttribute: 'pk'});
const ShortProfiel = new Schema('shortProfielen', {idAttribute: 'pk'});
const Werkgroep = new Schema('werkgroepen', {idAttribute: 'pk'});
const Kring = new Schema('kringen', {idAttribute: 'pk'});
const OverigeGroep = new Schema('overigeGroepen', {idAttribute: 'pk'});
const Verticale = new Schema('verticalen', {idAttribute: 'pk'});
const Commissie = new Schema('commissies', {idAttribute: 'pk'});
const Ondervereniging = new Schema('onderverenigingen', {idAttribute: 'pk'});

Profiel.define({
  kring: Kring,
  onderverenigingen: arrayOf(Ondervereniging),
  commissies: arrayOf(Commissie),
  verticale: Verticale,
  werkgroepen: arrayOf(Werkgroep),
  overige_groepen: arrayOf(OverigeGroep)
});

/* Action Creators */

//
// ProfielDetail
//

export let profielDetail = createDetailActions('Profiel', Profiel, api.profiel.get);

//
// ProfielList
//

export function requestProfielList(page, filter={}) {
  return {
    type: REQUEST_PROFIEL_LIST,
    metatype: meta.REQUEST_ENTITIES,
    page,
    filter
  };
}

export function receiveProfielList(response, filter={}) {
  return {
    type: RECEIVE_PROFIEL_LIST,
    metatype: meta.RECEIVE_ENTITIES,
    response: normalize(response, {data: { results: arrayOf(ShortProfiel)}}),
    filter: filter
  };
}

export function fetchProfielList(page, filter={}) {
  return dispatch => {
    dispatch(requestProfielList(page, filter));
    return api.profiel.list(page, filter)
      .catch((err) => console.error(err))
      .then(resp => {
        dispatch(receiveProfielList(resp, filter));
      });
  };
}

export function loadProfielList(page, filters={}) {
  return fetchProfielList(page, filters);
}
