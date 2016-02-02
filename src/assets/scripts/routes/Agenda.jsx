import React from "react";
import $ from "jquery";
import _ from "underscore";
import { Route, IndexRoute, Link } from 'react-router';

import Agenda from "../containers/Agenda";

export default (
  <Route>
    <IndexRoute component={Agenda} />
    <Route path="maand/:year/:month" component={Agenda} />
  </Route>
);
