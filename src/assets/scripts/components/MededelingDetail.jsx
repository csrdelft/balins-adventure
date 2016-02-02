import React from 'react';
import $ from 'jquery';
import _ from 'underscore';

import ProfielLink from '../components/ProfielLink';

export default class MededelingDetail extends React.Component {
  static get propTypes() {
    return {
      mededeling: React.PropTypes.object
    };
  }

  render() {
    let { mededeling } = this.props;

    if(mededeling) {
      return <div>
        <h1>{mededeling.titel}</h1>
        <ProfielLink pk={mededeling.user.pk}>{mededeling.user.full_name}</ProfielLink>
        <p>{mededeling.tekst}</p>
        </div>;
    } else {
      return <p>Loading... MededelingDetail</p>;
    }
  }
}
