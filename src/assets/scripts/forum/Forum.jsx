let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let { RouteHandler } = require('react-router');

let Layout = require("Layout");

class ForumSideMenu extends React.Component {
  render() {
    return (
      <ul>
        <li><h3>Algemeen</h3></li>
        <li><h3>Lichting 2013 (b'vo)</h3></li>
        <li><h3>Geloofszaken</h3></li>
        <li><h3>Nonsense</h3></li>
      </ul>
    );
  }
}

class Forum extends React.Component {
  render() {
    return (
      <Layout title="Reformaforum" sidemenu={<ForumSideMenu />}>
        <RouteHandler />
      </Layout>
    );
  }
}

module.exports = Forum;
