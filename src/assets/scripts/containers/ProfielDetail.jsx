import React from "react";
import $ from "jquery";
import _ from "underscore";

import Layout from "../components/Layout";
import LidPhoto from "../components/LidPhoto";

import api from "../utils/api";

class Profiel extends React.Component {

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      profiel: undefined
    };
  }

  update(pk) {
    api.profiel.get(pk)
      .then(
      (resp) => {
        console.debug("Profile loaded...");
        this.setState({profiel: resp.data});
      },
      (resp) => console.error('Getting profiel failed with status ' + resp.status)
    );
  }

  componentWillReceiveProps(nextProps) {
    if(this.props.params.pk != nextProps.params.pk) {
      this.update(nextProps.params.pk);
    }
  }

  componentWillMount() {
    this.update(this.props.params.pk);
  }

  template() {
    // helper to make setters for profiel attributes
    let profiel = this.state.profiel;

    // actual template based on the state
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
    if(this.state.profiel) {
      return (
        <Layout id="profiel-detail" title={`Profiel van ${this.state.profiel.full_name}`}>
          { this.template() }
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

module.exports = Profiel;
