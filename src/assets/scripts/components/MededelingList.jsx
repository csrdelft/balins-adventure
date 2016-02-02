import React from "react";
import $ from "jquery";
import _ from "underscore";
import { Router, Link } from 'react-router';

export default class MededelingList extends React.Component {

  static get propTypes() {
    return {
      mededelingen: React.PropTypes.array
    };
  }

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
