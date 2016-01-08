import React from 'react';
import { Link, Route, IndexRoute } from 'react-router';

import Profiel from './Profiel';
import ProfielList from './ProfielList';
import VerticaleList from './VerticaleList';
import VerticaleDetail from './VerticaleDetail';
import ProfielLink from './ProfielLink.jsx';

import mui from "material-ui";
import Layout from "Layout";
import CommissieList from "./CommissieList";
import KringList from "./KringList";

class Leden extends React.Component {

  render() {
    return <Layout title="Leden">
      <ul className="nav nav-tabs nav-justified">
        <li>
          <Link to="/leden">Ledenlijst</Link>
        </li>
        <li role="presentation">
          <Link to="/leden/groepen/verticale">Verticalen</Link>
        </li>
        <li role="presentation">
          <Link to="/leden/groepen/kring">Kringen</Link>
        </li>
        <li role="presentation">
          <Link to="/leden/groepen/commissie">Commissies</Link>
        </li>
        <li role="presentation">
          Besturen
        </li>
        <li role="presentation">
          Onderverenigingen
        </li>
      </ul>
      <div id="page-content">
        {this.props.children}
      </div>
    </Layout>;
  }
}

// wraps profiel list in the Leden layout
class LedenList extends React.Component {
  render() {
    return <Leden><ProfielList /></Leden>;
  }
}

export default <Route>
  <IndexRoute component={LedenList}/>

  <Route path="groepen" component={Leden}>
    <Route path="verticale" component={VerticaleList}/>
    <Route path="commissie" component={CommissieList}/>
    <Route path="kring" component={KringList}/>

  </Route>

  <Route path=":pk" component={Profiel}/>
  <Route path="verticale/:pk" component={VerticaleDetail}/>

</Route>;
