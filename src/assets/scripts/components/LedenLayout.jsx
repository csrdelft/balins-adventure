import React, {Component} from 'react';
import Layout from "../components/Layout";
import {Link} from 'react-router';

export default class LedenLayout extends Component {

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
