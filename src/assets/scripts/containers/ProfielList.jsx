import React from "react";
import $ from "jquery";
import _ from "underscore";
import { Link } from 'react-router';
import {InlineTextInput} from '../components/forms';
import LedenLayout from '../components/LedenLayout';
import * as actions from '../actions';
import { connect } from 'react-redux';
import qs from 'query-string';
import history from '../store/history';
import { fromJS } from 'immutable';

let loadData = _.throttle((props, filter) => {
  return props.dispatch(
    actions.profiel.loadList(Object.assign({}, {page: props.page}, filter))
  );
}, 1000);

export default class ProfielList extends React.Component {

  static get propTypes() {
    return {
      page: React.PropTypes.number.isRequired,
      shortProfielen: React.PropTypes.array.isRequired
    };
  }

  constructor(props) {
    super(props);

    this.state = {
      filter: this.props.initialFilter
    };

    this.onFilter = this.filter.bind(this);
  }

  componentWillMount() {
    loadData(this.props, this.state.filter);
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.page != this.props.page) {
      loadData(nextProps, this.state.filter);
    }
  }

  filter(name, value) {
    // create new filter object
    let nextFilter = Object.assign({}, this.state.filter);
    if(value == "") {
      delete nextFilter[name];
    } else {
      nextFilter[name] = value;
    }

    // update the state
    this.setState({
      filter: nextFilter
    });

    // update the url
    // we can push directly because we don't have to reload the page
    // we're only updating the query string for future reference
    history.push(
      Object.assign({}, location, {search: `?${qs.stringify(nextFilter)}`})
    );

    loadData(this.props, nextFilter);
  }

  render() {
    let { shortProfielen, page } = this.props;

    return (
      <LedenLayout>
        <div id="profiel-list">
          <div id="page-action-menu">
            <ul>
              <li className="action-input">
                <InlineTextInput
                  label="Zoeken..."
                  value={this.state.filter.search}
                  onChange={this.onFilter.bind(this, "search")}/>
              </li>
              <li className="action-input">
                <InlineTextInput
                  label="Lichting..."
                  value={this.state.filter.lichting}
                  onChange={this.onFilter.bind(this, "lichting")}/>
              </li>
              <li className="action-input">
                <InlineTextInput
                  label="Verticale..."
                  value={this.state.filter.verticale}
                  onChange={this.onFilter.bind(this, "verticale")}/>
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
                { _.map(shortProfielen, (profiel) => {
                    return <tr key={profiel.pk}>
                      <td>{profiel.pk}</td>
                      <td>
                          <Link to={`/leden/${profiel.pk}`}>
                            {profiel.full_name}
                          </Link>
                      </td>
                      <td>{profiel.email}</td>
                    </tr>
                  }
                )}
              </tbody>
            </table>
          </div>
        </div>
      </LedenLayout>
    );
  }
};

function select(state, props) {
  let page = parseInt(props.params.page) || 1;
  let initialFilter = props.location.query;
  let { entities: {shortProfielen}, shortProfielenByParams } = state;
  let ids = shortProfielenByParams.get(fromJS(
    Object.assign({}, initialFilter, {page: page})));
  let profielen = _(ids).map((id) => shortProfielen[id]);

  return {
    shortProfielen: profielen,
    page,
    initialFilter
  };
}

export default connect(select)(ProfielList);
