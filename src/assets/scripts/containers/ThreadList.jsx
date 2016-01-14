import React from "react";
import Reflux from "reflux";
import $ from "jquery";
import _ from "underscore";
import cs from "classnames";
import api from "../utils/api";
import moment from "moment";

import { Link } from 'react-router';
import ProfielLink from '../components/ProfielLink.jsx';
import ThreadForm from "../components/ThreadForm";
import ForumThreadList from "../components/ThreadList";
import actions from "../actions";

export default class ForumList extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      threads: [],
      show_create: false
    };
  }

  componentWillMount() {
  }


  update(pk, page=1) {
    actions.loadThreads(pk, page);
  }

  componentWillUnmount() {
    // make sure to unsubscribe from the thread store
    this.unsubscribe();
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.params.pk != this.props.params.pk || nextProps.params.page != this.props.params.page) {
      this.update(nextProps.params.pk, nextProps.params.page);
    }
  }

  showCreate(show=true) {
    this.setState({
      show_create: show
    });
  }

  deleteThread(thread_pk) {
    actions.deleteThread(thread_pk);
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
        <ForumThreadList threads={this.state.threads} />
       </div>
     </div>
    );
  }
}
