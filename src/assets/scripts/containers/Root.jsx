import React, {Component, PropTypes} from 'react';
import {connect} from 'react-redux';

// view components
import Menu from "../components/MainMenu";

class Root extends Component {

  static get propTypes() {
    return {
      user: PropTypes.object
    };
  }

  render() {
    return <div>
      <div id="global-nav">
        <Menu user={this.props.user} />
      </div>

      <div id="app">
        <div id="app-header-fill">
        </div>

        <div className="container-fluid">
          {this.props.children}
        </div>
      </div>
    </div>;
  }
}

function select(state) {
  let {entities: {shortProfielen}, auth: {currentUser}} = state;

  return {
    user: currentUser ? shortProfielen[currentUser] : undefined
  };
}

export default connect(select)(Root);
