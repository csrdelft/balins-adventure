import React from "react";
import $ from "jquery";
import _ from "underscore";
import api from "api";
import { Router, Link } from 'react-router';

let PropTypes = Router.PropTypes;

class MededelingList extends React.Component {

  render() {
    return <div>
      <h1>Mededelingen</h1>
      <ul>
        {
          _.map(this.props.mededelingen, (mededeling, i) =>
            <li key={mededeling.pk}>
              <Link to={`mededelingen/${mededeling.pk}`}>{mededeling.titel}</Link>
            </li>
          )
        }
      </ul>
    </div>;
  }
}

// the component takes an attribute to manipulate the update interval
MededelingList.propTypes = {
  mededelingen: React.PropTypes.arrayOf(React.PropTypes.object).isRequired
};

module.exports = MededelingList;
