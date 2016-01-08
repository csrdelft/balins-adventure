import React from "react";
import $ from "jquery";
import _ from "underscore";
import { State } from 'react-router';
import api from 'api';

import MededelingList from './MededelingList';
import Layout from "Layout";

class MededelingenSidemenu extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    return <MededelingList mededelingen={this.props.mededelingen} />;
  }
}

export default class Mededelingen extends React.Component {

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      mededelingen: []
    };

  }

  componentWillMount() {
    this.update();
  }

  update() {
    api.mededelingen.list()
      .then(
      (resp) => this.setState({mededelingen: resp.data}),
      (resp) => console.error('Getting mededelingen failed with status ' + resp.status)
    );
  }

  render() {
    let props = {mededelingen: this.state.mededelingen};

    return (
      <Layout title="Mededelingen" sidemenu={MededelingList} sidemenuProps={props}>
        {this.props.children}
      </Layout>
    );
  }
}
