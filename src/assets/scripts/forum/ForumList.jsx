let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let api = require("api");
let { Link, RouteHandler } = require('react-router');

let PostForm = require("forum/PostForm");

class ForumList extends React.Component {

  static get propTypes() {
    return { pk: React.PropTypes.string.isRequired }
  }

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    }
  }

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      threads: []
    };
  }

  update(pk) {
    // use the api to get most recent forum threads
    // this returns a promise that we can register our success and error callbacks on
    // at success we simply update the state of the component
    api.forum.threads.list(this.props.pk)
      .then(
        (resp) => this.setState({ threads: resp.data }),
        (resp) => console.error('Getting recent forum posts failed with status ' + resp.status)
      );
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.pk != this.props.pk) {
      this.update(nextProps.pk);
    }
  }

  componentWillMount() {
    // load initial recent forum posts
    this.update(this.props.pk);
  }

  render() {
    return (
      <div id="forum-thread">
        <div id="page-action-menu">
          <ul>
            <li>
              <button className="action">
                + draadje
              </button>
            </li>
          </ul>
        </div>

        <div id="page-content">
          <table>
            <tbody>
              { _.map(this.state.threads, (thread) => (
                  <tr key={thread.pk}>
                    <td>{thread.user.full_name}</td>
                    <td>
                      <Link to="forum-post-detail" params={{pk: thread.pk}}>
                        {thread.titel}
                      </Link>
                    </td>
                  </tr>
                ))
              }
            </tbody>
          </table>
        </div>
      </div>
    );
  }
}

module.exports = ForumList;
