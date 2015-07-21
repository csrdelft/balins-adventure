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

  render() {
    return <Layout title="Profiel">
      { this.state.profiel
          ? template(this, this.state.profiel)
          : <h1>Loading...</h1>
      }
    </Layout>;
  }
}

module.exports = Profiel;
