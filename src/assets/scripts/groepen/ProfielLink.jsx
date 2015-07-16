const React = require("react");
const $ = require("jquery");
const _ = require("underscore");
const api = require("api");
const PropTypes = require('react-router').PropTypes;
const Civikaartje = require("./Civikaartje");

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
			show_civikaartje: false,
			profiel: undefined
		};

		this.go = this.go.bind(this);
		this.link = this.link.bind(this);
		this.unlink = this.unlink.bind(this);
  }

	componentWillMount() {
    // load the profile
    api.profiel.get(this.uid)
      .then(
        (resp) => this.setState({profiel: resp.data}),
        (resp) => console.error('Getting profiel failed with status ' + resp.status)
      );
  }

	go(event) {
		this.context.router.transitionTo('profiel-detail', {uid: this.uid});
	}

	link() {
		this.setState({
			show_civikaartje: true
		});
	}

	unlink() {
		//Uses delay to let animation finish before hiding element
		const delay = 500;
		setTimeout(() => {
			this.setState({
			 show_civikaartje: false
		 });
		}, delay);
	}

	render_civikaartje() {
		if(this.state.show_civikaartje) {
			return (
				<div className="profielLinkHover" onMouseLeave={this.unlink.bind(this)} >
					  <Civikaartje profiel={this.state.profiel} />
				</div>
			);
		} else {
			return null;
		}
	}
	render() {
	  if(this.state.profiel) {
		  return (
		   <div className="profielLinkDiv"  >
			   <a className="profielLinkName" onClick={this.go} onMouseEnter={this.link.bind(this)} >
				   { this.state.profiel.full_name }
		     </a>
			   {this.render_civikaartje()}
		   </div>
		  );
		} else {
		  return <p>Loading...</p>;
		}
	}
}

ProfielLink.contextTypes = {
  router: React.PropTypes.func
};

module.exports = ProfielLink;
