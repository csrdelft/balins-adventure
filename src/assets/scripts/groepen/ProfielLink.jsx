const React = require("react");
const $ = require("jquery");
const _ = require("underscore");
const api = require("api");
const PropTypes = require('react-router').PropTypes;
const Civikaartje = require("./Civikaartje");
const Link = require('react-router');

class ProfielLink extends React.Component {

  static get propTypes() {
    return {
      pk: React.PropTypes.string.isRequired,
      name: React.PropTypes.string
    };
  }

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    }
  }

  constructor(props, context) {
    super(props, context);
    this.pk = props.pk;

    // initial state
		this.state = {
      show_civikaartje: false,
      profiel: undefined
    };

    this.link = this.link.bind(this);
    this.unlink = this.unlink.bind(this);
  }

  update(pk) {
    api.profiel.get(pk)
      .then(
      (resp) => this.setState({profiel: resp.data}),
      (resp) => console.error('Getting profiel failed with status ' + resp.status)
    );
  }

	componentWillMount() {
    this.update(this.pk);
  }

  componentWillReceiveProps(nextProps) {
    if(this.pk != nextProps.pk) {
      this.update(nextProps.pk);
    }
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
    if(this.state.show_civikaartje && this.state.profiel) {
      return (
       <div className="profielLinkHover" onMouseLeave={this.unlink.bind(this)} >
         <Civikaartje profiel={this.state.profiel} />
       </div>
      );
    } else {
      return <p>Loading...</p>;
    }
  }

  render() {
    if(this.state.profiel) {
      return (
       <div className="profielLinkDiv">
         <Link className="profielLinkName" to="profiel-detail" params={{pk: this.state.profiel.pk}} onMouseEnter={this.link.bind(this)}>
           { this.state.profiel.full_name }
         </Link>
         {this.render_civikaartje()}
       </div>
      );
    } else {
      return <p>Loading...</p>;
    }
  }
}

module.exports = ProfielLink;
