let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let mixin = require("mixin");
let { RouteHandler, State } = require('react-router');

let MededelingList = require('./MededelingList');
let Layout = require("Layout");

class MededelingenSidemenu extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return <MededelingList mededelingen={this.props.mededelingen} />;
  }
}

class Mededelingen extends React.Component {

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      mededelingen: []
    };

  }

  componentWillMount() {
    this.update();
  }

  update() {
    api.mededelingen.list()
      .then(
      (resp) => this.setState({mededelingen: resp.data}),
      (resp) => console.error('Getting mededelingen failed with status ' + resp.status)
    );
  }

  render() {
    let props = {mededelingen: this.state.mededelingen};

    return (
      <Layout title="Mededelingen"
        sidemenu={MededelingList} sidemenuProps={props}
      >
        <RouteHandler {...this.props.params} />
      </Layout>
    );
  }
}

module.exports = Mededelingen;
