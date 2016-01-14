import React from 'react';
import { connect } from 'redux';
import $ from 'jquery';
import _ from 'underscore';
import moment from 'moment';

import { Link } from 'react-router';
import ProfielLink from '../components/ProfielLink';
import PostForm from '../components/PostForm';

import * as actions from '../actions';

export class ForumPost extends React.Component {

  static get propTypes() {
    return {
      post: React.PropTypes.object.isRequired,
      dispatch: React.PropTypes.func.isRequired
    };
  }

  deletePost() {
    // just kick off the delete action
    this.props.dispatch(
      actions.forumDraad.deletePost(this.props.post.pk)
    );
  }

  render() {
    let post = this.props.post;
    let author = this.props.post.user;

    return (
      <tr key={post.pk}>
        <th>
          <ProfielLink pk={author.pk}>{author.full_name}</ProfielLink>
          <i>{moment(post.laatst_gewijzigd).fromNow()}</i>
          <div className="post-actions">
            { post.can_delete
              ? <button onClick={this.deletePost.bind(this, post.pk)}>X</button>
              : false
            }
          </div>
        </th>
        <td>{post.tekst}</td>
      </tr>
    );
  }
}

export default class ForumThread extends React.Component {

  static get propTypes() {
    return {
      pk: React.PropTypes.number.isRequired,
      last_page: React.PropTypes.number.isRequired,
      page: React.PropTypes.number.isRequired,
      draadje: React.PropTypes.object.isRequired,
      posts: React.PropTypes.array.isRequired,
      dispatch: React.PropTypes.func.isRequired
    };
  }

  static get defaultProps() {
    return {
      page: "1"
    };
  }

  renderPageLinks() {
    // build the page links
    let min_page = Math.max(parseInt(this.props.page) - 4, 1);
    let max_page = Math.min(parseInt(this.props.page) + 4, this.props.last_page);
    let pages = _.map(_.range(min_page, max_page + 1), (pageno) => [pageno, pageno]);
    if(min_page > 1)
      pages.unshift([1, "<<"]);
    if(max_page < this.props.last_page)
      pages.push([this.props.last_page, ">>"]);

    return pages.map((page) =>
      <Link
        key={page}
        className="action" to="forum-draadje-detail-page"
        params={{pk: this.props.pk, page: page[0]}}>
          {page[1]}
      </Link>
    );
  }

  render() {
    return (
      <div id="forum-draadje">
        <div id="page-action-menu">
          <ul>
            <li>
              <button className="action">
                <strong>+</strong> bericht
              </button>
              {this.renderPageLinks()}
            </li>
          </ul>
        </div>

        <div id="page-content">
          <table>
            <tbody>
              { _.map(this.props.posts, (p) =>
                  // don't render deleted items
                  <ForumPost post={p} key={p.pk} dispatch={this.props.dispatch} />
                )
              }
            </tbody>
          </table>

          <PostForm draadje={this.props.pk} draadjePage={this.props.page} />
        </div>
      </div>
    );
  }
}
