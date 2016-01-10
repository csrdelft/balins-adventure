import React from "react";
import $ from "jquery";
import _ from "underscore";
import { connect } from "react-redux";
import * as actions from '../actions';

import Layout from "../components/Layout";
import LidPhoto from "../components/LidPhoto";

import api from "../utils/api";

function loadData(props) {
  const { pk } = props;
  actions.loadProfielDetail(pk);
}

class ProfielDetail extends React.Component {

  componentWillMount() {
    console.debug("Loading profile");
    loadData(this.props);
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.pk !== this.props.pk) {
      loadData(nextProps.pk);
    }
  }

  renderProfiel() {
    let { profiel, dispatch } = this.props;

    return (
      <div>
        <h1>
          {profiel.voornaam} {profiel.tussenvoegsel} {profiel.achternaam}
        </h1>
        <h3>
          A.K.A. {profiel.nickname}
        </h3>
        <div className="gegevens">
          <LidPhoto size="lg" pk={profiel.pk} />
          <table className="table table-bordered">
            <tbody>
            <tr>
              <td>Verticale</td>
              <td>{ profiel.verticale.naam }</td>
            </tr>
            <tr>
              <td>Kring</td>
              <td>{ profiel.kring ? profiel.kring.naam : "Geen" }</td>
            </tr>
            </tbody>
          </table>
        </div>

        <div className="commissies">
          <h2>Commissies</h2>
          <table className="table table-bordered">
            <tbody>
            { _.map(profiel.commissies, (c, i) =>
              <tr key={i}><td>{ c.naam }</td></tr>
            )}
            </tbody>
          </table>

          <h2>Werkgroepen</h2>
          <table className="table table-bordered">
            <tbody>
            { _.map(profiel.werkgroepen, (c, i) =>
              <tr key={i}><td>{ c.naam }</td></tr>
            )}
            </tbody>
          </table>

          <h2>Overige Groepen</h2>
          <table className="table table-bordered">
            <tbody>
            { _.map(profiel.groepen, (c, i) =>
              <tr key={i}><td>{ c.naam }</td></tr>
            )}
            </tbody>
          </table>
        </div>
      </div>
    );
  }

  render() {
    if(this.props.profiel) {
      return (
        <Layout id="profiel-detail" title={`Profiel van ${this.state.profiel.full_name}`}>
          { this.renderProfiel() }
        </Layout>
      );
    } else {
      return (
        <Layout title="Profiel van ...">
          <h1>Loading...</h1>
        </Layout>
      );
    }
  }
}

function select(state, props) {
  let { pk } = props.params;
  let { entities: { profielen }} = state;

  let profiel = profielen[pk] || undefined;

  return {
    profiel
  };
}

export default connect(select)(ProfielDetail);
