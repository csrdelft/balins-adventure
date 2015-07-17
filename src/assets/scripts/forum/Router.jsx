let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let { Route, DefaultRoute, Link, RouteHandler } = require('react-router');

let Forum = require("forum/Forum");
let ForumList = require("forum/ForumList");
let ForumThread = require("forum/ForumThread");

module.exports = (
  <Route handler={Forum}>
    <Route path="parts">
      <Route path=":pk" name="forum-thread-list" handler={ForumList}/>
      <Route path=":pk/:page" name="forum-thread-list-page" handler={ForumList}/>
    </Route>

    <Route path="threads">
      <Route path=":pk" name="forum-thread-detail" handler={ForumThread}/>
      <Route path=":pk/:page" name="forum-thread-detail-page" handler={ForumThread}/>
    </Route>
  </Route>
);
