let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let { Route, DefaultRoute, Link, RouteHandler } = require('react-router');

let Forum = require("forum/Forum");
let ForumList = require("forum/ForumList");
let ForumDraad = require("forum/ForumDraad");

module.exports = (
  <Route handler={Forum}>
    <Route path=":pk" name="forumthread-list" handler={ForumList}/>
    <Route path="threads/:pk" name="forum-detail" handler={ForumDraad}/>
  </Route>
);
