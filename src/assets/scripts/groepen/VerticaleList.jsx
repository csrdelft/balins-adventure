let React = require('react');
let { Link } = require('react-router');
let _ = require("underscore");
let actions = require("./actions");
let stores = require("./stores");

class VerticaleList extends React.Component {

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
                  <td>{vert.aantal_leden}</td>
                </tr>
            )
        }
        </tbody>
      </table>
    </div>;
  }
}

module.exports = VerticaleList;
