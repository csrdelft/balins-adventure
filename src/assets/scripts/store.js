import { compose, createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import routes from './routes';
import DevDock from './containers/DevDock';

export default function configureStore(rootReducer, initialState, ...middleware) {
  let finalCreateStore =
    // compose multiple store enhancers
    compose(
      applyMiddleware(thunk, ...middleware),
      DevDock.instrument()
    )(createStore);

  return finalCreateStore(rootReducer, initialState);
}
