import React from "react";
import $ from "jquery";
import _ from "underscore";
import { connect } from "react-redux";
import * as actions from '../actions';

import Layout from "../components/Layout";
import LidPhoto from "../components/LidPhoto";

import api from "../utils/api";

class ProfielDetail extends React.Component {

  // Method to load the target profile into the store
  loadData() {
    const { pk } = this.props.params;
    this.props.dispatch(actions.loadProfielDetail(pk));
  }

  componentWillMount() {
    // make sure that the profile is loaded on mount
    this.loadData(this.props);
  }

  componentWillReceiveProps(nextProps) {
    // We have to reload our profile if the primary key from the route changes
    if (nextProps.params.pk !== this.props.params.pk) {
      this.loadData(nextProps.pk);
    }
  }

  renderProfiel() {
    let {
      profiel,
      verticale,
      commissies,
      kring,
      overigeGroepen,
      onderverenigingen,
      werkgroepen,
      dispatch
    } = this.props;

    return (
      <div>
        <h1>
          {profiel.voornaam} {profiel.tussenvoegsel} {profiel.achternaam}
        </h1>
        <h3>
          A.K.A. {profiel.nickname}
        </h3>
        <div className="gegevens">
          <LidPhoto size="lg" pk={profiel.id} />
          <table className="table table-bordered">
            <tbody>
            <tr>
              <td>Verticale</td>
              <td>{ verticale ? verticale.naam : "Geen" }</td>
            </tr>
            <tr>
              <td>Kring</td>
              <td>{ kring ? kring.naam : "Geen" }</td>
            </tr>
            </tbody>
          </table>
        </div>

        <div className="commissies">
          <h2>Commissies</h2>
          <table className="table table-bordered">
            <tbody>
            { _.map(commissies, (c, i) =>
              <tr key={i}><td>{ c.naam }</td></tr>
            )}
            </tbody>
          </table>

          <h2>Werkgroepen</h2>
          <table className="table table-bordered">
            <tbody>
            { _.map(werkgroepen, (c, i) =>
              <tr key={i}><td>{ c.naam }</td></tr>
            )}
            </tbody>
          </table>

          <h2>Overige Groepen</h2>
          <table className="table table-bordered">
            <tbody>
            { _.map(overigeGroepen, (c, i) =>
              <tr key={i}><td>{ c.naam }</td></tr>
            )}
            </tbody>
          </table>
        </div>
      </div>
    );
  }

  render() {
    // only render if profile is loaded
    if(this.props.profiel) {
      return (
        <Layout id="profiel-detail" title={`Profiel van ${this.props.profiel.full_name}`}>
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

// select everything from the global store that is relevant to
// profiel detail
function select(state, props) {
  let { pk } = props.params;
  let { entities: {
    profielen,
    commissies,
    onderverenigingen,
    kringen,
    overigeGroepen,
    verticalen,
    werkgroepen
  }} = state;

  let profiel = profielen[pk];
  let profielRelations = profiel ? {
    kring: kringen[profiel.kring],
    verticale: verticalen[profiel.verticale],
    commissies: _.map(profiel.commissies, (id) => commissies[id]),
    overigeGroepen: _.map(profiel.overigeGroepen, (id) => overigeGroepen[id]),
    werkgroepen: _.map(profiel.werkgroepen, (id) => werkgroepen[id]),
    onderverenigingen: _.map(profiel.onderverenigingen, (id) => werkgroepen[id])
  } : {};

  return Object.assign({profiel: profiel}, profielRelations);
}

// Using redux we 'connect' ProfielDetail to the store through the select function.
// All selected state is injected into the props of ProfielDetail.
// Everytime the store is updated, the properties will update and React will make sure
// that ProfielDetail re-renders.
export default connect(select)(ProfielDetail);
