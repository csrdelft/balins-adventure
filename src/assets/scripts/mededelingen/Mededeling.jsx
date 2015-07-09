var React = require("react");
var $ = require("jquery");
var _ = require("underscore");
var api = require("api");

class Mededeling extends React.Component {
  constructor(props) {
    super(props);

    // initial state
    this.state = {
      mededeling: {}
    };
  }

  update() {
    api.mededelingen.get_mededeling(this.props.params.id)
      .then(
      (resp) => this.setState({mededeling: resp.data}),
      (resp) => console.error('Getting mededeling failed with status ' + resp.status)
    );
  }

  componentDidMount() {
    // load initial recent forum posts
    this.update();
  }

  render() {
    let mededeling = this.state.mededeling;
    return (
      <div>
        <h1>{mededeling.titel}</h1>

        <p>{mededeling.tekst}</p>
      </div>
    );
  }
}

module.exports = Mededeling;
