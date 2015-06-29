var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

var api = require("api");

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
    var p = this.state.profiel;

    if(this.state.profiel) {
      var html = (
        <div>
          <h1>{ p.full_name }</h1>
          <div class="gegevens">
            <table class="table table-bordered">
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

          <div class="commissies">
            <h2>Commissies</h2>
            <ul>
              { _.map(p.commissies, (c) => <li>{ c.naam }</li>) }
            </ul>

            <h2>Werkgroepen</h2>
            <ul>
              { _.map(p.werkgroepen, (w) => <li>{ w.naam }</li>) }
            </ul>

            <h2>Overige Groepen</h2>
            <ul>
              { _.map(p.groepen, (g) => <li>{ g.naam }</li>) }
            </ul>
          </div>
        </div>
      );
    } else {
      var html = <h1>Loading...</h1>;
    }

    return html;
  }
}

Profiel.propTypes = { profiel: React.PropTypes.number };

module.exports = Profiel;
