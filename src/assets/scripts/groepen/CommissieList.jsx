import React from 'react';
import _ from "underscore";
import { Link } from 'react-router';
import api from "api";
import actions from "./actions";
import stores from "./stores";
import LidPhoto from "groepen/LidPhoto";
import moment from "moment";
import queryString from "query-string";

export default class CommissieList extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      commissies: [],
      families: [],
      filter: {}
    };
  }

  componentDidMount() {
    // parse initial filter
    // and default it
    let filter = _.chain(queryString.parse(window.location.search))
      .pick('familie')
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

  render() {
    let commissies = _(this.state.commissies)
      .chain()
      .groupBy('status')
      .mapObject((comms, status) =>
         <div>
          <h1>{status}</h1>
          <table className="table table-bordered table-striped">
            <tbody>
              {
                _(comms).map((c) => <tr key={c.pk}><td>{c.naam}</td></tr>)
              }
            </tbody>
          </table>
        </div>
      )
      .value();

    let familie_options = _(this.state.families)
      .map((fam) => <option key={fam} value={fam}>{fam}</option>);
    familie_options.unshift(<option key={-1} value="">-- Familie --</option>);

    return (
     <div id="commissie-list">
       <div id="page-action-menu">
         <ul>
           <li>
             <select onChange={this.handleFamilieChange.bind(this)} defaultValue={this.state.filter.familie}>
               { familie_options }
             </select>
           </li>
         </ul>
       </div>

       <div id="page-content">
         {commissies.ft ? commissies.ft : null}
         {commissies.ht ? commissies.ht : null}
         {commissies.ot ? commissies.ot : null}
       </div>
     </div>
    );
  }
}
