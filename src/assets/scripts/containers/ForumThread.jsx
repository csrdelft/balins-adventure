import React, {Component, PropTypes} from 'react';
import { connect } from 'react-redux';
import $ from 'jquery';
import _ from 'underscore';
import moment from 'moment';
import DumbForumThread from '../components/ForumThread';
import {Map, fromJS} from 'immutable';

import * as actions from '../actions';

function loadData(props) {
  let { dispatch, pk, page } = props;
  dispatch(actions.forumDraad.load(pk, {page}));
}

class ForumThread extends Component {

  static get propTypes() {
    return {
      pk: React.PropTypes.number.isRequired,
      last_page: React.PropTypes.number.isRequired,
      page: React.PropTypes.number.isRequired,
      draadje: React.PropTypes.object,
      posts: React.PropTypes.array.isRequired
    };
  }

  componentWillMount() {
    loadData(this.props);
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.pk !== this.props.pk) {
      loadData(nextProps);
    }
  }

  render() {
    let props = this.props;

    if(props.draadje && props.posts !== undefined) {
      return <DumbForumThread
        pk={props.pk}
        last_page={props.last_page}
        page={props.page}
        draadje={props.draadje}
        posts={props.posts}
        dispatch={props.dispatch} />;
    } else {
      return <h1>Draadjes laden...</h1>;
    }
  }

}

function select(state, props) {
  var { pk , page } = props.params;
  pk = parseInt(pk);
  page = parseInt(page || 1);

  let {
    entities: {draadjes, posts},
    postsByThreadParams
  } = state;

  let draadje = draadjes[pk];
  let draadje_posts = _.chain(postsByThreadParams.get(fromJS({pk, page})) || [])
    .map((id) => posts[id])
    .filter((post) => !post._isDeleted)
    .value();

  return {
    draadje,
    posts: draadje_posts,
    pk: pk,
    page: page,
    last_page: 1 // TODO
  };
}

export default connect(select)(ForumThread);
