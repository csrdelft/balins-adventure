import initialState from '../store';

export function entities(state = {
    profielen: {},
    kringen: {},
    commissies: {},
    onderverenigingen: {},
    verticalen: {},
    overigeGroepen: {},
    werkgroepen: {}
  }, action) {
  if(action.response && action.response.entities) {
    return Object.assign({}, state, action.response.entities);
  }

  return state;
};
