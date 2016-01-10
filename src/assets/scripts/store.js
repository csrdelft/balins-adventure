import { createStore, applyMiddleware } from 'redux';
import routes from 'routes';
import thunk from 'redux-thunk';

export default function configureStore(rootReducer, initialState, ...middleware) {
  let finalCreateStore = applyMiddleware(thunk, ...middleware)(createStore);
  return finalCreateStore(rootReducer, initialState);
}
