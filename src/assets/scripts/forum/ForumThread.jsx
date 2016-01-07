let React = require("react");
let Reflux = require("reflux");
let $ = require("jquery");
let _ = require("underscore");
let Layout = require("Layout");
let { Link, RouteHandler } = require('react-router');
let moment = require("moment");

let ProfielLink = require("groepen/ProfielLink");
let PostForm = require("forum/PostForm");
let api = require("api");
let stores = require("forum/stores");
let actions = require("forum/actions");

class ForumPost extends React.Component {

  static get propTypes() {
    return {
      post: React.PropTypes.object.isRequired,
      threadPage: React.PropTypes.string.isRequired
    };
  }

  constructor(props) {
    super(props);
  }

  deletePost() {
    // just kick off the delete action
    // and make sure to reload the right thread page afterwards
    // we have to do it here because the store won't know which page to load
    actions
      .deletePost(this.props.post.pk)
      .then(() => {
        return actions.loadThread(this.props.post.draad, this.props.threadPage);
      });
  }

  render() {
    let post = this.props.post;
    return (
      <tr key={post.pk}>
        <th>
          <ProfielLink pk={post.user.pk}>{post.user.full_name}</ProfielLink>
          <i>{moment(post.laatst_gewijzigd).fromNow()}</i>
          <div className="post-actions">
            { post.can_delete
              ? <button onClick={this.deletePost.bind(this)}>X</button>
              : false
            }
          </div>
        </th>
        <td>{post.tekst}</td>
      </tr>
    );
  }
}

class ForumThread extends React.Component {

  static get propTypes() {
    return {
      // strings (route parameters)
      pk: React.PropTypes.string.isRequired,
      page: React.PropTypes.string
    };
  }

  static get defaultProps() {
    return {
      page: "1"
    };
  }

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    }
  }

  constructor(props, context) {
    super(props, context);

    // initial state
    this.state = {
      thread: undefined,
      last_page: 1
    };
  }

  update(pk, page) {
    actions.loadThread(pk, page);
  }

  componentWillReceiveProps(nextProps) {
    if(this.props.pk != nextProps.pk || this.props.page != nextProps.page) {
      this.update(nextProps.pk, nextProps.page);
    }
  }

  componentWillMount() {
    // listen to thread store
    stores.threadDetailStore.listen((threads) => {
      let thread = threads[this.props.pk];
      this.setState({
        thread: thread,
        last_page: thread.last_page
      });
    });

    // kick of fresh thread load
    this.update(this.props.pk, this.props.page);
  }

  render() {
    let min_page = Math.max(parseInt(this.props.page) - 4, 1);
    let max_page = Math.min(parseInt(this.props.page) + 4, this.state.last_page);
    let pages = _.map(_.range(min_page, max_page + 1), (pageno) => [pageno, pageno]);
    if(min_page > 1)
      pages.unshift([1, "<<"]);
    if(max_page < this.state.last_page)
      pages.push([this.state.last_page, ">>"]);
    let page_links = pages.map((page) =>
      <Link key={page} className="action" to="forum-thread-detail-page"
        params={{pk: this.props.pk, page: page[0]}}>{page[1]}</Link>);

    // make sure that the thread and the right posts page are loaded
    if(this.state.thread && this.state.thread.posts[this.props.page]) {
      let posts_page = this.state.thread.posts[this.props.page];
      return (
        <div id="forum-thread">
          <div id="page-action-menu">
            <ul>
              <li>
                <button className="action">
                  <strong>+</strong> bericht
                </button>
                {page_links}
              </li>
            </ul>
          </div>

          <div id="page-content">
            <table>
              <tbody>
                { _.map(posts_page.results, (p) =>
                    <ForumPost threadPage={this.props.page} post={p} key={p.pk} /> )
                }
              </tbody>
            </table>
            <PostForm thread={this.props.pk} threadPage={this.props.page} />
          </div>
        </div>
      );
    } else {
      return <h1>Loading...</h1>;
    }
  }
}

module.exports = ForumThread;
