const React = require("react");
const $ = require("jquery");
const _ = require("underscore");
const api = require("api");
const PropTypes = require('react-router').PropTypes;

class ProfielLink extends React.Component {

	static get propTypes() {
    return {
			uid: React.PropTypes.number.isRequired,
			name: React.PropTypes.string
		};
  }

	constructor(props, context) {
		super(props);
		this.context = context;
		this.uid = props.uid;

		// initial state
		this.state = {
			profiel: undefined
		};

		this.go = this.go.bind(this)
  }

	componentWillMount() {
    // load the profile
    api.base.get_profiel(this.uid)
      .then(
        (resp) => this.setState({profiel: resp.data}),
        (resp) => console.error('Getting profiel failed with status ' + resp.status)
      );
  }

	go(event) {
		this.context.router.transitionTo('profiel-detail', {uid: this.uid});
	}

	render() {
	  if(this.state.profiel) {
		  return <a data-id={this.props.uid} onClick={this.go}>{ this.state.profiel.full_name }</a>;
		} else {
		  return <p>Loading...</p>;
		}
	}
}

ProfielLink.contextTypes = {
  router: React.PropTypes.func
};

module.exports = ProfielLink;
