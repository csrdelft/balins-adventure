import { compose, createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import routes from '../routes';
import DevDock from '../containers/DevDock';
import { syncHistory, routeReducer } from 'react-router-redux';
import history from './history';

export default function configureStore(rootReducer, initialState, ...middleware) {
  let reduxRouterMiddleware = syncHistory(history);
  let finalCreateStore =
    // compose multiple store enhancers
    compose(
      applyMiddleware(
        thunk,
        reduxRouterMiddleware,
        ...middleware
      ),
      DevDock.instrument()
    )(createStore);

  let store = finalCreateStore(rootReducer, initialState);
  reduxRouterMiddleware.listenForReplays(store);

  return store;
}
