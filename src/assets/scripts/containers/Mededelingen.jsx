import React from "react";
import $ from "jquery";
import _ from "underscore";
import { State } from 'react-router';
import {connect} from 'react-redux';
import api from '../utils/api';

import MededelingList from '../components/MededelingList';
import Layout from "../components/Layout";

class Mededelingen extends React.Component {

  static get propTypes() {
    return {
      mededelingen: React.PropTypes.array
    };
  }

  render() {
    let props = {mededelingen: this.props.mededelingen};

    return (
      <Layout title="Mededelingen" sidemenu={MededelingList} sidemenuProps={props}>
        {this.props.children}
      </Layout>
    );
  }
}

function select(state) {
  let { entities: {mededelingen}} = state;

  return {
    mededelingen: [] 
  };
}

export default connect(select)(Mededelingen);
