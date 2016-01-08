import React from "react";
import $ from "jquery";
import _ from "underscore";
import { Route, IndexRoute, Link } from 'react-router';

import Forum from "forum/Forum";
import ForumList from "forum/ForumList";
import ForumThread from "forum/ForumThread";

module.exports = (
  <Route component={Forum}>
    <IndexRoute component={null} />

    <Route path="parts">
      <Route path=":pk" component={ForumList}/>
      <Route path=":pk/:page" component={ForumList}/>
    </Route>

    <Route path="threads">
      <Route path=":pk" component={ForumThread}/>
      <Route path=":pk/:page" component={ForumThread}/>
    </Route>
  </Route>
);
