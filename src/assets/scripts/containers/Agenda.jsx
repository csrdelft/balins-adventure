import React, { Component, PropTypes } from "react";
import $ from "jquery";
import _ from "underscore";
import cs from "classnames";
import api from "../utils/api";
import moment from "moment";
import { connect } from 'react-redux';

import * as actions from '../actions';
import Layout from "../components/Layout";
import Calendar from "../components/Calendar";

function loadData(props) {
  let { dispatch, month, year } = props;
}

class Agenda extends Component {

  static get propTypes() {
    return {
      year: PropTypes.number.isRequired,
      month: PropTypes.number.isRequired,
      events: PropTypes.array.isRequired
    };
  }

  monthChanged(year, month) {
    console.debug("Month changed:", year, month);
  }

  render() {
    return <Layout id="agenda" title={`Agenda`}>
        <Calendar
          initFocus={moment([this.props.year, this.props.month, 1])}
          events={this.props.events}
          onMonthChange={this.monthChanged.bind(this)} />
      </Layout>;
  }
}

function select(state, props) {
  let { year, month } = props.params;

  return {
    year: parseInt(year || moment().format("YYYY")),
    month: parseInt(month || moment().format("MM")),
    events: [{
      startdatetime: moment([2016, 2, 4, 13, 0]).format(),
      enddatetime: moment([2016, 2, 4, 15, 0]).format(),
      title: "Lunchen met het bestuur"
    },{
      startdatetime: moment([2016, 2, 8, 17, 0]).format(),
      enddatetime: moment([2016, 2, 8, 24, 0]).format(),
      title: "SURPRISE HV"
    }]
  };
}

export default connect(select)(Agenda);
