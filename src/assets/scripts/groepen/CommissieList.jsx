let React = require('react');
let { Link } = require('react-router');
let _ = require("underscore");
let actions = require("./actions");
let stores = require("./stores");
let LidPhoto = require("groepen/LidPhoto");
let moment = require("moment");
let queryString = require("query-string");

class CommissieList extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      commissies: undefined,
      filter: {}
    };
  }

  componentDidMount() {
    // parse initial filter
    // and default it
    let filter = _.chain(queryString.parse(window.location.search))
          .pick('status', 'familie')
          .defaults({
            status: "ht"
          })
          .value();

    // save the filter state
    this.setState({filter: filter});

    // load the data
    actions
      .loadCommissies(filter)
      .then(
        (resp) => this.setState({commissies: resp.data})
      );
  }

  render() {
    return (
     <div id="commissie-list">
       <div id="page-action-menu">
         <ul>
           <li>
           </li>
         </ul>
       </div>

       <div id="page-content">
         <table className="table table-bordered table-striped">
           <tbody>
             {
               _.map(this.state.commissies, (c) =>
                 <tr>
                    <td>{c.naam}</td>
                    <td>{c.status}</td>
                 </tr>
               )
             }
           </tbody>
         </table>
       </div>
     </div>
    );
  }
}

module.exports = CommissieList;
