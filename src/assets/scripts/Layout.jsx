import React from "react";
import $ from "jquery";
import _ from "underscore";

export default class Layout extends React.Component {

  renderSidemenu() {
    if(this.props.sidemenu) {
      return (
        <div id="side-column" className="col-xs-3">
          <div id="side-header-fill">
          </div>

          <div id="page-menu">
            <this.props.sidemenu {...this.props.sidemenuProps} />
          </div>
        </div>
      );
    } else {
      return <i></i>;
    }
  }

  render() {
    return (
      <div className="row">

        { this.renderSidemenu() }

        <div id="content-column" className={this.props.sidemenu ? "col-xs-9" : "col-xs-12" }>
          <div id="header-bg"></div>
          <div id="page-container">
            <h1>{this.props.title}</h1>
            <div id="page">
              {this.props.children}
            </div>
          </div>
        </div>
      </div>
    );
  }
}
