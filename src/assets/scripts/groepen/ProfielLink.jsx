const React = require("react");
const $ = require("jquery");
const _ = require("underscore");

var api = require("api");

class ProfielLink extends React.Component {

	constructor(props) {
		super(props);

    // initial state
    this.state = {
    	uid: this.props.params.uid,
			profiel: undefined,
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

		this.setState({name: this.state.profiel.achternaam})
  }

	static get propTypes = () => {
    return {
			uid: React.PropTypes.number.isRequired,
			name: React.PropTypes.string
		};
  };

	render() {
		return <Link to="/profiel/" this.state.uid>this.state.name</Link>
	}
}

module.exports = ProfielLink;