import React from 'react';
import { Link } from 'react-router';
import _ from "underscore";
import api from "api";
import actions from "./actions";
import stores from "./stores";
import LidPhoto from "groepen/LidPhoto";
import moment from "moment";
import queryString from "query-string";

export default class KringList extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      kringen: [],
      familie: undefined,
      families: []
    };
  }

  componentWillMount() {
    // load the data
    actions
      .loadKringen(this.state.filter);
  }

  componentDidMount() {
    this.setState({
      kringen: stores.kringListStore.getAll(),
      families: stores.kringListStore.getFamilieChoices()
    });

    stores.kringListStore.listen((kringen) => 
      // save the filter state
      // and load data
      this.setState({
        kringen: kringen,
        families: stores.kringListStore.getFamilieChoices()
      })
    );
  }

  handleFamilieChange(e) {
    this.setState({
      familie: e.target.value
    });
  }

  render() {
    let kringen = this.state.kringen;
    if(this.state.familie) {
      kringen = _.filter(kringen, (k) => k.familie == this.state.familie);
    }

    return (
     <div id="kringen-list">
       <div id="page-action-menu">
         <ul>
           <li>
             <select defaultValue={this.state.familie}
                     onChange={this.handleFamilieChange.bind(this)}>
               <option key={-1} value="">
                 -- Verticale --
               </option>
               { _.map(this.state.families, (v) =>
                 <option key={v}>{v}</option>
               )}
             </select>
           </li>
         </ul>
       </div>

       <div id="page-content">
         <table className="table table-bordered table-striped">
           <tbody>
             {
               _.map(kringen, (k) =>
                 <tr key={k.pk}>
                    <td>{k.familie}</td>
                    <td>{k.naam}</td>
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
