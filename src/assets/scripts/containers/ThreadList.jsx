import React, { Component, PropTypes } from "react";
import $ from "jquery";
import _ from "underscore";
import cs from "classnames";
import api from "../utils/api";
import moment from "moment";
import { connect } from 'react-redux';
import { fromJS } from 'immutable';

import ThreadForm from "../components/ThreadForm";
import ForumThreadList from "../components/ThreadList";

import * as actions from '../actions';

function loadData(props) {
  let { dispatch, page, pk } = props;
  dispatch(actions.forumDraad.loadList({ pk, page }));
}

class ThreadList extends React.Component {

  static get propTypes() {
    return {
      page: React.PropTypes.number.isRequired,
      pk: React.PropTypes.number.isRequired,
      threads: React.PropTypes.array.isRequired
    };
  }

  constructor(props) {
    super(props);
    this.state = {
      show_create: false
    };
  }

  componentWillMount() {
    loadData(this.props);
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.page != this.props.page || nextProps.pk != this.props.pk) {
      this.update(nextProps);
    }
  }

  showCreate(show=true) {
    this.setState({
      show_create: show
    });
  }

  render() {
    let create_classes = cs({
      open: this.state.show_create
    });

    return (
     <div id="forum-thread-list">
       <div id="page-action-menu">
         <ul>
           <li>
             <button className="action" onClick={this.showCreate.bind(this, true)}>
               + draadje
             </button>
           </li>
         </ul>
       </div>

       <div id="thread-form" className={create_classes} >
         <h2>Nieuw draadje</h2>
         <ThreadForm forum={this.props.params.pk} onCancel={this.showCreate.bind(this, false)}/>
       </div>

       <div id="page-content">
        <ForumThreadList threads={this.props.threads} />
       </div>
     </div>
    );
  }
}

function select(state, props) {
  let { pk } = props.params;
  let page = 1;
  let { entities: { shortDraadjes }, shortDraadjesByParams } = state;
  let ids = shortDraadjesByParams.get(fromJS({pk, page})) || [];
  let threads = _.map(ids, (id) => shortDraadjes[id]);

  return {
    page: page,
    pk,
    threads: threads
  };
}

export default connect(select)(ThreadList);
