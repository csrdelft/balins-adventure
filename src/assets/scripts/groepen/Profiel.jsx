var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

var api = require("api");
var template = require("templates/Profiel");

class Profiel extends React.Component {

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      uid: this.props.uid,
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
    if(this.state.profiel) {
      return (
        <Layout title="Profiel">
          template(this, this.state.profiel)
        </Layout>
      );
    } else {
      return <h1>Loading...</h1>;
    }
  }
}

Profiel.propTypes = { profiel: React.PropTypes.number };

module.exports = Profiel;
