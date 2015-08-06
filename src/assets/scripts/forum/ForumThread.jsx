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
      threadPage: React.PropTypes.number.isRequired
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
          <div class="post-actions">
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
      thread: undefined
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
      this.setState({
        thread: threads[this.props.pk]
      });
    });

    // kick of fresh thread load
    this.update(this.props.pk, this.props.page);
  }

  render() {
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
                <Link className="action" to="forum-thread-detail-page"
                  params={{pk: this.props.pk, page: Math.max(1, parseInt(this.props.page) - 1)}} >
                  &lt;
                </Link>
                <Link className="action" to="forum-thread-detail-page"
                  params={{pk: this.props.pk, page: parseInt(this.props.page) + 1}} >
                  &gt;
                </Link>
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
