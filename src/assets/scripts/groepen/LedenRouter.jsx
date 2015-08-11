let React = require('react');
let { Link, Route, DefaultRoute, RouteHandler} = require('react-router');

let Profiel = require('./Profiel');
let ProfielList = require('./ProfielList');
let VerticaleList = require('./VerticaleList');
let VerticaleDetail = require('./VerticaleDetail');
let ProfielLink = require('./ProfielLink.jsx');

let mui = require("material-ui");
let Layout = require("Layout");
let LedenList = require("./ProfielList");

class Leden extends React.Component {

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    };
  }
  
  render() {
    return <Layout title="Leden">
      <ul className="nav nav-tabs nav-justified">
        <li>
          <Link to="leden">Ledenlijst</Link>
        </li>
        <li role="presentation">
          <Link to="verticale-list">Verticalen</Link>
        </li>
        <li role="presentation">
          Kringen
        </li>
        <li role="presentation">
          Commissies
        </li>
        <li role="presentation">
          Besturen
        </li>
        <li role="presentation">
          Onderverenigingen
        </li>
      </ul>
      <div id="page-content">
        <RouteHandler />
      </div>
    </Layout>;
  }
}

module.exports =
  <Route>
    <Route handler={Leden}>
      <DefaultRoute name='leden-list' handler={ProfielList}/>

      <Route name='verticale-list' path="verticale" handler={VerticaleList}/>

    </Route>

		<Route name='profiel-detail' path=":pk" handler={Profiel}/>
    <Route name='verticale-detail' path="verticale/:pk" handler={VerticaleDetail}/>

  </Route>;
