const React = require("react");
const $ = require("jquery");
const _ = require("underscore");

var api = require("api");

class ProfielLink extends React.Component {

	static get propTypes() {
    return {
			uid: React.PropTypes.number.isRequired,
			name: React.PropTypes.string
		};
  }

	constructor(props) {
		super(props);

    // initial state
    this.state = {
      // TODO uid is not mutable state, it's constant, so no need to be in state
    	uid: this.props.uid,
			profiel: undefined,
			// TODO name is part of profiel, no need to duplicate in state
			name: undefined
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
	    // TODO implement go (look at MededelingList.jsx, requires a router in context)
		  return <a  data-id={this.props.uid} onClick={this.go}>{ this.state.profiel.achternaam }</a>;
		} else {
		  return <p>Loading...</p>;
		}
	}
}

module.exports = ProfielLink;
