import api from '../utils/api';
import { normalize, Schema, arrayOf } from 'normalizr';
import createDetailActions from './createDetailActions';
import createListActions from './createListActions';
import * as meta from './meta';

function paginated(schema) {
  return {
    results: arrayOf(schema)
  };
};

// Action types:
// Used to identify the action uniquely from the listeners (i.e. reducers)
export const RECEIVE_PROFIEL = 'RECEIVE_PROFIEL';
export const REQUEST_PROFIEL = 'REQUEST_PROFIEL';
export const RECEIVE_PROFIEL_LIST = 'RECEIVE_PROFIEL_LIST';
export const REQUEST_PROFIEL_LIST = 'REQUEST_PROFIEL_LIST';

// Schemas
// Describe the JSON structure that we get back from the API.
// Primarily used to normalize the nested reponses into a flat structure using normalizr
export const Profiel = new Schema('profielen', {idAttribute: 'pk'});
export const ShortProfiel = new Schema('shortProfielen', {idAttribute: 'pk'});
export const Werkgroep = new Schema('werkgroepen', {idAttribute: 'pk'});
export const Kring = new Schema('kringen', {idAttribute: 'pk'});
export const OverigeGroep = new Schema('overigeGroepen', {idAttribute: 'pk'});
export const ShortVerticale = new Schema('shortVerticalen', {idAttribute: 'pk'});
export const Verticale = new Schema('verticalen', {idAttribute: 'pk'});
export const Commissie = new Schema('commissies', {idAttribute: 'pk'});
export const Ondervereniging = new Schema('onderverenigingen', {idAttribute: 'pk'});

Profiel.define({
  kring: Kring,
  onderverenigingen: arrayOf(Ondervereniging),
  commissies: arrayOf(Commissie),
  verticale: ShortVerticale,
  werkgroepen: arrayOf(Werkgroep),
  overige_groepen: arrayOf(OverigeGroep)
});

/* Action Creators */

export let profiel = Object.assign({},
  createDetailActions('Profiel', Profiel, api.profiel.get),
  createListActions('Profiel', paginated(ShortProfiel), api.profiel.list)
);

export let verticale = Object.assign({},
  createListActions('Verticale', arrayOf(Verticale), api.verticalen.list)
);

export let commissie = Object.assign({},
  createListActions('Verticale', arrayOf(Verticale), api.verticalen.list)
);
