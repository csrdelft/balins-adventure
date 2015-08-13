let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let Layout = require("Layout");
let LidPhoto = require("groepen/LidPhoto");

let api = require("api");

class Profiel extends React.Component {

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    }
  }

  static get propTypes() {
    return { pk: React.PropTypes.string.isRequired };
  }

  constructor(props, context) {
    super(props, context);

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
        this.setState({profiel: resp.data})
      },
      (resp) => console.error('Getting profiel failed with status ' + resp.status)
    );
  }

  componentWillReceiveProps(nextProps) {
    if(this.props.pk != nextProps.pk) {
      this.update(nextProps.pk);
    }
  }

  componentWillMount() {
    this.update(this.props.pk);
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
            <tr>
              <td>Verticale</td>
              <td>{ profiel.verticale.naam }</td>
            </tr>
            <tr>
              <td>Kring</td>
              <td>{ profiel.kring ? profiel.kring.naam : "Geen" }</td>
            </tr>
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
