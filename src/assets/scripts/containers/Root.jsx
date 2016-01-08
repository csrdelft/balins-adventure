import React, {Component} from 'react';

// view components
import Menu from "../components/MainMenu";

export default class Root extends Component {

  render() {
    return <div>
      <div id="global-nav">
        <Menu />
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
