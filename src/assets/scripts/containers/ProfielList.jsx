import React from "react";
import $ from "jquery";
import _ from "underscore";
import { Link } from 'react-router';
import {InlineTextInput} from '../components/forms';
import LedenLayout from '../components/LedenLayout';
import * as actions from '../actions';
import { connect } from 'react-redux';

function loadData(props, filters) {
  return props.dispatch(
    actions.loadProfielList(props.page, filters)
  );
}

export default class ProfielList extends React.Component {

  static get propTypes() {
    return {
      page: React.PropTypes.number.isRequired,
      shortProfielen: React.PropTypes.object.isRequired,
      shortProfielenByFilter: React.PropTypes.object.isRequired,
    };
  }

  constructor(props) {
    super(props);
    this.state = {
      filters: {}
    };

    this.onFilter = _.throttle(this.filter, 1000).bind(this);
  }

  componentWillMount() {
    loadData(this.props, this.state.filters);
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.page != this.props.page) {
      loadData(nextProps, this.state.filters);
    }
  }

  filter(name, value) {
    // create new filters object
    let filters = Object.assign({}, this.state.filters);
    if(value == "") {
      delete filters[name];
    } else {
      filters[name] = value;
    }

    // update the state
    this.setState({
      filters: filters
    });

    loadData(this.props, filters);
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
                  onChange={this.onFilter.bind(this, "search")}/>
              </li>
              <li className="action-input">
                <InlineTextInput
                  label="Lichting..."
                  onChange={this.onFilter.bind(this, "lichting")}/>
              </li>
              <li className="action-input">
                <InlineTextInput
                  label="Verticale..."
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
                { _.map(shortProfielenByFilter.get(this.state.filters), (id) => {
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
    page
  };
}

export default connect(select)(ProfielList);
