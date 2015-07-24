let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let api = require("api");
let { Link, RouteHandler } = require('react-router');

let ProfielLink = require('../groepen/ProfielLink.jsx')
let ThreadForm = require("./ThreadForm");

class ForumList extends React.Component {

  static get propTypes() {
    return {
      // because passed as route parameter, these are strings
      pk: React.PropTypes.string.isRequired,
      page: React.PropTypes.string
    }
  }

  static get defaultProps() {
    return {
      page: "1"
    }
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
      threads: []
    };
  }

  update(pk, page=1) {
    // use the api to get most recent forum threads
    // this returns a promise that we can register our success and error callbacks on
    // at success we simply update the state of the component
    api.forum.threads.list(pk, page)
      .then(
        (resp) => this.setState({ threads: resp.data }),
        (resp) => console.error('Getting recent forum posts failed with status ' + resp.status)
      );
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.pk != this.props.pk || nextProps.page != this.props.page) {
      this.update(nextProps.pk, nextProps.page);
    }
  }

  componentWillMount() {
    // load initial recent forum posts
    this.update(this.props.pk);
  }

  render() {
    return (
     <div id="forum-thread-list">
       <div id="page-action-menu">
         <ul>
           <li>
             <button className="action">
               + draadje
             </button>
             <Link className="action" to="forum-thread-list-page"
                   params={{pk: this.props.pk, page: Math.max(1, parseInt(this.props.page) - 1)}}>
               &lt;
             </Link>
             <Link className="action" to="forum-thread-list-page"
                   params={{pk: this.props.pk, page: parseInt(this.props.page) + 1}}>
               &gt;
             </Link>
           </li>
         </ul>
       </div>

       <div id="thread-form">
         <ThreadForm forum={this.props.pk} />
       </div>

       <div id="page-content">
         <table>
           <tbody>
           { _.map(this.state.threads, (thread) => (
            <tr key={thread.pk}>
              <th><ProfielLink pk={thread.user.pk}>{thread.user.full_name}</ProfielLink></th>
              <td>
                <Link to="forum-thread-detail" params={{pk: thread.pk}}>
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
