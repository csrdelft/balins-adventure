let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let Layout = require("Layout");

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
          {profiel.voornaam}
          &nbsp;
          {profiel.tussenvoegsel}
          &nbsp;
          {profiel.achternaam}
        </h1>
        <h3>
          A.K.A.
          &nbsp;
          {profiel.nickname}
        </h3>
        <div className="gegevens">
          <table className="table table-bordered">
            <tr>
              <th>Verticale</th>
              <td>{ profiel.verticale.naam }</td>
            </tr>
            <tr>
              <th>Kring</th>
              <td>{ profiel.kring.naam }</td>
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
    return <Layout title="Profiel">
      { this.state.profiel
          ? this.template()
          : <h1>Loading...</h1>
      }
    </Layout>;
  }
}

module.exports = Profiel;
