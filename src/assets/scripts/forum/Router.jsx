let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let { Route, DefaultRoute, Link, RouteHandler } = require('react-router');

let Forum = require("forum/Forum");
let ForumList = require("forum/ForumList");
let ForumDraad = require("forum/ForumDraad");

module.exports = (
  <Route handler={Forum}>
    <DefaultRoute name="forum-list" handler={ForumList}/>
    <Route name="forum-detail" path=":id" handler={ForumDraad}/>
  </Route>
);
