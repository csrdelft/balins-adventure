import React, { PropTypes, Component } from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router';
import _ from "underscore";
import LidPhoto from "../components/LidPhoto";

import * as actions from "../actions";

function loadData(props) {
  let { dispatch } = props;
  dispatch(actions.verticale.loadList());
}

class VerticaleList extends Component {

  static get propTypes() {
    return {
      verticalen: PropTypes.object.isRequired
    };
  }

  componentWillMount() {
    loadData(this.props);
  }

  render() {
    return <div id="verticale-list">
      <table className="table table-bordered table-striped">
        <thead>
          <th>Naam</th>
          <th>Aantal leden</th>
        </thead>
        <tbody>
        {
            _.map(this.props.verticalen, (vert) => 
                <tr key={vert.pk}>
                  <td>
                    <Link to="verticale-detail" params={{pk: vert.pk}}>{vert.naam}</Link>
                  </td>
                  <td>{
                    _.map(vert.leden, (lid) =>
                      <LidPhoto size="sm" key={lid.user.pk} pk={lid.user.pk} name={lid.user.full_name} />
                    )
                  }</td>
                </tr>
            )
        }
        </tbody>
      </table>
    </div>;
  }
}

function select(state) {
  let { verticalen } = state.entities;

  return {
    verticalen
  };
}

export default connect(select)(VerticaleList);
