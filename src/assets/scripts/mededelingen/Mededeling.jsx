var React = require("react");
var $ = require("jquery");
var _ = require("underscore");
var api = require("api");

class Mededeling extends React.Component {

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      threads: []
    };

    this.interval = null;
  }

  update() {
    // use the api to get most recent forum threads
    // this returns a promise that we can register our success and error callbacks on
    // at success we simply update the state of the component
    api.mededelingen.get_mededeling(0)
      .then(
        (resp) => this.setState({ threads: resp.data }),
        (resp) => console.error('Getting recent forum posts failed with status ' + resp.status)
      );
  }

  componentDidMount() {
    // load initial recent forum posts
    this.update();
  }

  componentWillUnmount() {
    // make sure we unset the update at interval
    // at the end of the component lifecycle
    window.clearInterval(this.interval);
  }

  render() {
    // map the state to HTML
    return <div>
      {
        _.map(this.state.threads,
          (thread, i) => <h3 key={i}>{thread.titel}</h3>
        )
      }
      </div>;
  }
}

// the component takes an attribute to manipulate the update interval
Mededeling.propTypes = { updateInterval: React.PropTypes.number };
Mededeling.defaultProps = { updateInterval: 60000 };

module.exports = Mededeling;
