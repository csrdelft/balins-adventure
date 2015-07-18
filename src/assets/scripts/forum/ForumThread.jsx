let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let Layout = require("Layout");
let { Link, RouteHandler } = require('react-router');
let ProfielLink = require("../groepen/ProfielLink");
let api = require("api");

class ForumPost extends React.Component {

  constructor(props) {
    super(props);
  }

  render() {
    let post = this.props.post;
    return (
      <tr key={post.pk}>
        <th><ProfielLink pk={post.user.pk}>{post.user.full_name}</ProfielLink></th>
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

  update(pk, page=1) {
    api.forum.threads.get(pk, page)
      .then(
      (resp) => this.setState({thread: resp.data}),
      (resp) => console.error('Getting thread failed with status ' + resp.status)
    );
  }

  componentWillReceiveProps(nextProps) {
    if(this.props.pk != nextProps.pk || this.props.page != nextProps.page) {
      this.update(nextProps.pk, nextProps.page);
    }
  }

  componentWillMount() {
    this.update(this.props.pk);
  }

  render() {
    if(this.state.thread) {
      return (
        <div id="forum-thread">
          <div id="page-action-menu">
            <ul>
              <li>
                <button className="action">
                  + draadje
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
              {_.map(this.state.thread.posts, (p) => <ForumPost post={p} key={p.pk} /> )}
            </tbody>
          </table>
          </div>
        </div>
      );
    } else {
      return <h1>Loading...</h1>;
    }
  }
}

module.exports = ForumThread;
