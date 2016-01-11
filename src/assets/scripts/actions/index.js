import api from '../utils/api';
import { normalize, Schema, arrayOf } from 'normalizr';

export const RECEIVE_PROFIEL = 'RECEIVE_PROFIEL';
export const REQUEST_PROFIEL = 'REQUEST_PROFIEL';

const Profiel = new Schema('profielen');
const Werkgroep = new Schema('werkgroepen');
const Kring = new Schema('kringen');
const OverigeGroep = new Schema('overigeGroepen');
const Verticale = new Schema('verticalen');
const Commissie = new Schema('commissies');
const Ondervereniging = new Schema('onderverenigingen');

Profiel.define({
  kring: Kring,
  onderverenigingen: arrayOf(Ondervereniging),
  commissies: arrayOf(Commissie),
  verticale: Verticale,
  werkgroepen: arrayOf(Werkgroep),
  overige_groepen: arrayOf(OverigeGroep)
});

//
// ProfielDetail
//

export function requestProfielDetail(pk) {
  return {
    type: REQUEST_PROFIEL,
    pk
  };
}

export function receiveProfielDetail(response) {
  return {
    type: RECEIVE_PROFIEL,
    response: normalize(response, {data: Profiel})
  };
}

export function fetchProfielDetail(pk) {
  return dispatch => {
    dispatch(requestProfielDetail(pk));
    return api.profiel.get(pk)
      .catch((err) => console.error(err))
      .then(data => {
        dispatch(receiveProfielDetail(data));
      });
  };
}

export function loadProfielDetail(pk) {
  // optional cache retrieval can be done here
  return fetchProfielDetail(pk);
}
