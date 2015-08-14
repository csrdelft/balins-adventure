let React = require('react');
let { Link } = require('react-router');
let _ = require("underscore");
let api = require("api");
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
      families: [],
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

    // load the metadata
    // this only happens once for the page
    api.commissies
      .metadata()
      .then((resp) => this.setState({ families: resp.data.families }));

    // save the filter state
    // and load data
    this.setState({filter: filter}, () => this.update());
  }

  update() {
    // load the data
    actions
      .loadCommissies(this.state.filter)
      .then(
        (resp) => this.setState({commissies: resp.data})
      );
  }

  handleFamilieChange(e) {
    this.setState({
      filter: _.defaults({
        familie: e.target.value
      }, this.state.filter)
    }, () => this.update());
  }

  handleStatusChange(e) {
    this.setState({
      filter: _.defaults({
        status: e.target.value
      }, this.state.filter)
    }, () => this.update());
  }

  render() {
    return (
     <div id="commissie-list">
       <div id="page-action-menu">
         <ul>
           <li>
             <select onChange={this.handleFamilieChange.bind(this)}>
               <option value=""
                       selected={this.state.filter.familie == ""}>
                 -- Familie --
               </option>
               { _.map(this.state.families, (fam) =>
                 <option selected={this.state.filter.familie == fam}>{fam}</option>
               )}
             </select>
           </li>
           <li>
             <select onChange={this.handleStatusChange.bind(this)}>
               <option value="ot">OT</option>
               <option value="ht" selected={true}>HT</option>
               <option value="ft">FT</option>
             </select>
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
