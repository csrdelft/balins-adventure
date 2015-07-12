var React = require("react");
var $ = require("jquery");
var _ = require("underscore");
var api = require("api");

class MededelingBeheer extends React.Component {
  constructor(props, context) {
    super(props);

    this.context = context;

    // initial state
    this.state = {
      mededeling: {}
    };

    this.remove = this.remove.bind(this);
  }

  remove(event) {
    api.mededelingen.remove_mededeling(this.state.mededeling.id)
    .then(
      (resp) => this.context.router.transitionTo('mededeling-beheer'),
      (resp) => console.error(`Failed to remove mededeling with status code ${resp.status}`)
    );
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

        <a onClick={this.remove}>Verwijder</a>
      </div>
    );
  }
}

MededelingBeheer.contextTypes = {
  router: React.PropTypes.func
};

module.exports = MededelingBeheer;
