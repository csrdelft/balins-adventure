import React from "react";
import $ from "jquery";
import _ from "underscore";
import { Link } from 'react-router';
import {InlineTextInput} from '../components/forms';
import LedenLayout from '../components/LedenLayout';
import * as actions from '../actions';
import { connect } from 'react-redux';
import { pushPath } from 'redux-simple-router';
import qs from 'query-string';

let loadData = _.throttle((props, filter) => {
  return props.dispatch(
    actions.loadProfielList(props.page, filter)
  );
}, 1000);

export default class ProfielList extends React.Component {

  static get propTypes() {
    return {
      page: React.PropTypes.number.isRequired,
      shortProfielen: React.PropTypes.object.isRequired,
      shortProfielenByFilter: React.PropTypes.object.isRequired,
      initialFilter: React.PropTypes.object.isRequired
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
    this.props.dispatch(
      pushPath(Object.assign({}, location, {search: `?${qs.stringify(nextFilter)}`}))
    );

    loadData(this.props, nextFilter);
  }

  render() {
    let { shortProfielen, page, shortProfielenByFilter } = this.props;

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
                { _.map(shortProfielenByFilter.get(this.state.filter), (id) => {
                    let profiel = shortProfielen[id];
                    return <tr key={id}>
                      <td>{profiel.id}</td>
                      <td>
                          <Link to={`/leden/${profiel.id}`}>
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
  let { entities: {shortProfielen}, shortProfielenByFilter } = state;
  return {
    shortProfielen,
    shortProfielenByFilter,
    page,
    initialFilter: props.location.query
  };
}

export default connect(select)(ProfielList);
