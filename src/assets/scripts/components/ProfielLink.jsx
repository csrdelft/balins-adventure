import React from "react";
import $ from "jquery";
import _ from "underscore";

import Civikaartje from "./Civikaartje";
import {Link} from 'react-router';

export default class ProfielLink extends React.Component {

  static get propTypes() {
    return {
      pk: React.PropTypes.string.isRequired,
      name: React.PropTypes.string
    };
  }

  constructor(props) {
    super(props);
    this.pk = props.pk;
    this.name = props.children;

    // initial state
		this.state = {
      show_civikaartje: false
    };

    this.link = this.link.bind(this);
    this.unlink = this.unlink.bind(this);
  }

  link() {
    this.setState({
      show_civikaartje: true
    });
  }

  unlink() {
    //Uses delay to let animation finish before hiding element
    const delay = 500;
    window.setTimeout(() => {
      this.setState({
        show_civikaartje: false
      });
    }, delay);
  }

  render_civikaartje() {
    if(this.state.show_civikaartje) {
      return (
       <div className="profielLinkHover" onMouseLeave={this.unlink.bind(this)} >
         <Civikaartje pk={this.pk} />
       </div>
      );
    } else {
      return <div></div>;
    }
  }

  render() {
    return (
      <div className="profielLinkDiv">
        <Link
           className="profielLinkName"
           to={`/leden/${this.pk}`}
           onMouseEnter={this.link.bind(this)}>
          { this.name }
        </Link>
        {this.render_civikaartje()}
      </div>
    );
  }
}
