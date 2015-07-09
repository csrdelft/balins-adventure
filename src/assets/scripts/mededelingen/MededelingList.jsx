var React = require("react");
var $ = require("jquery");
var _ = require("underscore");
var api = require("api");


var mixin = require('es6-react-mixins');

var PropTypes = require('react-router').PropTypes;

class MededelingList extends React.Component {


  constructor(props, context) {
    super(props);

    this.context = context;

    // initial state
    this.state = {
      mededelingen: []
    };

    this.interval = null;

    this.go = this.go.bind(this)
  }

  go(event) {
    let id = $(event.target).data('id');
    this.context.router.transitionTo("mededeling-detail", {id: id});
  }

  update() {
    // use the api to get most recent forum threads
    // this returns a promise that we can register our success and error callbacks on
    // at success we simply update the state of the component
    api.mededelingen.get_list()
      .then(
      (resp) => {
        this.setState({mededelingen: resp.data});
      },
      (resp) => console.error('Getting recent forum posts failed with status ' + resp.status)
    );
  }

  componentDidMount() {
    // load initial recent forum posts
    this.update();

    // set the regular update
    this.interval = window.setInterval(() => this.update(), this.props.updateInterval);
  }

  componentWillUnmount() {
    // make sure we unset the update at interval
    // at the end of the component lifecycle
    window.clearInterval(this.interval);
  }

  render() {
    // map the state to HTML
    return <div>
      <h1>Mededelingen</h1>
      <ul>
        {
          _.map(this.state.mededelingen, (mededeling, i) => {
            return <li>
              <a data-id={mededeling.id} onClick={this.go}>{mededeling.titel}</a>
            </li>
          })
        }
      </ul>
    </div>;
  }
}

MededelingList.contextTypes = {
  router: React.PropTypes.func
};

// the component takes an attribute to manipulate the update interval
MededelingList.propTypes = {updateInterval: React.PropTypes.number};
MededelingList.defaultProps = {updateInterval: 60000};

module.exports = MededelingList;
