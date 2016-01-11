import { createStore, applyMiddleware } from 'redux';
import routes from 'routes';
import thunk from 'redux-thunk';

export default function configureStore(rootReducer, initialState, ...middleware) {
  let finalCreateStore = applyMiddleware(thunk)(createStore);
  return finalCreateStore(rootReducer, initialState);
}
