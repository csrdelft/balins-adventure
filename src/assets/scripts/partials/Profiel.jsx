var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

var api = require("api");

class InlineInput extends React.Component {

  constructor(props) {
    super(props);

    this.value = this.props.value;
    this.setter = this.props.setter;

    this.state = {
      editing: false
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleFocus = this.handleFocus.bind(this);
    this.handleBlur = this.handleBlur.bind(this);
  }

  handleChange(event) {
    this.setter(event.target.value);
  }

  handleFocus(event) {
    this.setState({editing: true});
  }

  handleBlur(event) {
    this.setState({editing: false});
  }

  render() {
    if(this.state.editing) {
      return <input type="text"
        defaultValue={this.value}
        onChange={this.handleChange}
        onBlur={this.handleBlur}
        autoFocus />;
    } else {
      return <span onDoubleClick={this.handleFocus} >{this.value}</span>;
    }
  }
}

class Profiel extends React.Component {

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      uid: this.props.params.uid,
      profiel: undefined
    };
  }

  componentWillMount() {
    // load the profile
    api.base.get_profiel(this.state.uid)
      .then(
        (resp) => this.setState({profiel: resp.data}),
        (resp) => console.error('Getting profiel failed with status ' + resp.status)
      );
  }

  render() {
    // shortcut to profiel current state
    let p = this.state.profiel;

    // helper to make setters for profiel attributes
    let self = this;
    function setter(attr) {
      return (v) => self.setState(_.extend(self.state.profiel, {[attr]: v}));
    }

    if(this.state.profiel) {
      return (
        <div>
          <h1>
            <InlineInput value={p.voornaam} setter={setter("voornaam")}/>
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
              { _.map(p.commissies, (c, i) =>
                <tr key={i}><td>{ c.naam }</td></tr>
              )}
            </table>

            <h2>Werkgroepen</h2>
            <table className="table table-bordered">
              { _.map(p.werkgroepen, (c, i) =>
                <tr key={i}><td>{ c.naam }</td></tr>
              )}
            </table>

            <h2>Overige Groepen</h2>
            <table className="table table-bordered">
              { _.map(p.groepen, (c, i) =>
                <tr key={i}><td>{ c.naam }</td></tr>
              )}
            </table>
          </div>
        </div>
      );
    } else {
      return <h1>Loading...</h1>;
    }
  }
}

Profiel.propTypes = { profiel: React.PropTypes.number };

module.exports = Profiel;
