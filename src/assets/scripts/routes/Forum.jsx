import React from "react";
import $ from "jquery";
import _ from "underscore";
import { Route, IndexRoute, Link } from 'react-router';

import Forum from "containers/Forum";
import ThreadList from "../containers/ThreadList";
import ForumThread from "../containers/ForumThread";

export default (
  <Route component={Forum}>
    <IndexRoute component={null} />

    <Route path="forums">
      <Route path=":pk" component={ThreadList}/>
      <Route path=":pk/:page" component={ThreadList}/>
    </Route>

    <Route path="draadjes">
      <Route path=":pk" component={ForumThread}/>
      <Route path=":pk/:page" component={ForumThread}/>
    </Route>
  </Route>
);
