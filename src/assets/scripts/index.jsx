import React from "react";
import $ from "jquery";
import { render } from 'react-dom';

import configureStore from 'store';
import App from 'containers/App';

let store = configureStore();

render(<App store={store} /> , $('#mount-app')[0]);

