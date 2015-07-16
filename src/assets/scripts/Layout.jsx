var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

class Layout extends React.Component {

  constructor(props) {
    super(props);
  }

  sidemenu() {
    if(this.props.sidemenu) {
      return (
        <div id="side-column" className="col-xs-3">
          <div id="side-header-fill">
          </div>

          <div id="page-menu">
            {this.props.sidemenu}
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

        { this.sidemenu() }

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

module.exports = Layout;
