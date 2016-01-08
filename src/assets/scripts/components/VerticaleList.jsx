import React from 'react';
import { Link } from 'react-router';
import _ from "underscore";
import actions from "./actions";
import stores from "./stores";
import LidPhoto from "groepen/LidPhoto";

export default class VerticaleList extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      verticalen: []
    };
  }
  
  componentWillMount() {
    actions.loadVerticalen();
  }

  componentDidMount() {
    this.setState({verticalen: stores.verticaleListStore.getAll()});
    this.unsubscribe = stores.verticaleListStore.listen((verticalen) => this.setState({
      verticalen: verticalen
    }));
  }

  componentWillUnmount() {
    this.unsubscribe();
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
            _.map(this.state.verticalen, (vert) => 
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
