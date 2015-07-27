let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let Layout = require("Layout");

let api = require("api");
let template = require("templates/Profiel");

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
      (resp) => this.setState({profiel: resp.data}),
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
    let setter = (attr) => {
      return (v) => this.setState(_.extend(this.state.profiel, {[attr]: v}));
    }

    // actual template based on the state
    return (
      <div>
        <h1>
          <InlineInput value={p.voornaam} setter={setter("voornaam")}/>
          &nbsp;
          <InlineInput value={p.tussenvoegsel} setter={setter("tussenvoegsel")}/>
          &nbsp;
          <InlineInput value={p.achternaam} setter={setter("achternaam")}/>
        </h1>
        <h3>
          A.K.A.
          &nbsp;
          <InlineInput value={p.nickname} setter={setter("nickname")}/>
        </h3>
        <div className="gegevens">
          <table className="table table-bordered">
            <tr>
              <th>Verticale</th>
              <td>{ p.verticale.naam }</td>
            </tr>
            <tr>
              <th>Kring</th>
              <td>{ p.kring.naam }</td>
            </tr>
          </table>
        </div>

        <div className="commissies">
          <h2>Commissies</h2>
          <table className="table table-bordered">
            <tbody>
            { _.map(p.commissies, (c, i) =>
              <tr key={i}><td>{ c.naam }</td></tr>
            )}
            </tbody>
          </table>

          <h2>Werkgroepen</h2>
          <table className="table table-bordered">
            <tbody>
            { _.map(p.werkgroepen, (c, i) =>
              <tr key={i}><td>{ c.naam }</td></tr>
            )}
            </tbody>
          </table>

          <h2>Overige Groepen</h2>
          <table className="table table-bordered">
            <tbody>
            { _.map(p.groepen, (c, i) =>
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
