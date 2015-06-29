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
      return (v) => console.log(v) && self.setState(_.extend(self.state.profiel, {[attr]: v}));
    }

    if(this.state.profiel) {
      return template(this.state.profiel, setter);
    } else {
      return <h1>Loading...</h1>;
    }
  }
}

Profiel.propTypes = { profiel: React.PropTypes.number };

module.exports = Profiel;
