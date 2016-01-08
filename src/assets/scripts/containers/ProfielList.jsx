import React from "react";
import $ from "jquery";
import _ from "underscore";
import { Link } from 'react-router';
import {InlineTextInput} from '../components/forms';
import LedenLayout from '../components/LedenLayout';

export default class ProfielList extends React.Component {

  static get propTypes() {
    // string because it's a route parameter
    return {page: React.PropTypes.string};
  }

  static get defaultProps() {
    return {page: "1"};
  }

  constructor(props) {
    super(props);

    this.search_text = "";
    this.filters = {};

    this.state = {
      profielen: [],
      search_profielen: [],
      searching: false
    };
  }

  componentWillMount() {
    // kick of initial load
    // actions.loadProfielen(this.props.page);
  }

  componentDidMount() {
    // initial data
    // this.setState({profielen: stores.profielListStore.getAll()});
    // listen to updates to the profielen list store
    // this.unsubscribe = stores.profielListStore
      // .listen((profielen) => this.setState({profielen: profielen}));
  }

  componentWillUnmount() {
    // this.unsubscribe();
  }

  componentWillReceiveProps(nextProps) {
    //if(nextProps.page != this.props.page) {
      // load the next page
      // actions.loadProfielen(nextProps.page);
    //}
  }

  search(search_text) {
    this.search_text = search_text;
    this.do_search(this.search_text, this.filters);
  }

  filter(name, value) {
    if(value == "") {
      delete this.filters[name];
    } else {
      this.filters[name] = value;
    }

    this.do_search(this.search_text, this.filters);
  }

  do_search(search_text, filters) {
    if(search_text === "" && filters === {}) {
      // go back to usual paged mode
      this.setState({
        searching: false,
        search_profielen: []
      });
    } else {
      // conduct the search
      actions
        .searchProfielen(search_text, filters)
        .then((resp) => {
          this.setState({
            searching: true,
            search_profielen: resp.data.results
          });
        })
        .done();
    }
  }

  render() {
    let profielen;
    if(this.state.searching)
      profielen = this.state.search_profielen;
    else
      profielen = this.state.profielen[this.props.page];

    return (
      <LedenLayout>
        <div id="profiel-list">
          <div id="page-action-menu">
            <ul>
              <li className="action-input">
                <InlineTextInput
                  label="zoeken..."
                  onChange={_.throttle(this.search, 500).bind(this)}/>
              </li>
              <li className="action-input">
                <InlineTextInput
                  label="lichting..."
                  onChange={_.throttle(this.filter, 500).bind(this, "lichting")}/>
              </li>
            </ul>
          </div>

          <div id="profiel-table">
            <table className="table table-bordered table-striped">
              <thead>
                <tr>
                  <th>Lidno.</th>
                  <th>Naam</th>
                  <th>E-mail</th>
                </tr>
              </thead>
              <tbody>
                { _.map(profielen, (profiel) => (
                    <tr key={profiel.pk}>
                      <td>{profiel.pk}</td>
                      <td>
                          <Link to="profiel-detail" params={{pk: profiel.pk}}>
                            {profiel.full_name}
                          </Link>
                      </td>
                      <td>{profiel.email}</td>
                    </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </LedenLayout>
    );
  }
};
