let React = require("react");
let Reflux = require("reflux");
let $ = require("jquery");
let _ = require("underscore");
let cs = require("classnames");
let api = require("api");
let mixin = require("mixin");
let moment = require("moment");

let { Link, RouteHandler } = require('react-router');
let ProfielLink = require('groepen/ProfielLink.jsx')
let ThreadForm = require("forum/ThreadForm");
let stores = require("forum/stores");
let actions = require("forum/actions");

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
      threads: {},
      show_create: false
    };
  }

  componentWillMount() {
    // subscribe at the thread store
    this.unsubscribe = stores
      .threadListStore
      .listen((threads) =>
        this.setState({
          threads: stores.threadListStore.getForumPage(this.props.pk, this.props.page)
        })
      );

    // force fresh load of forum threads
    this.update(this.props.pk, this.props.page);
  }


  update(pk, page=1) {
    actions.loadThreads(pk, page);
  }

  componentWillUnmount() {
    // make sure to unsubscribe from the thread store
    this.unsubscribe();
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.pk != this.props.pk || nextProps.page != this.props.page) {
      this.update(nextProps.pk, nextProps.page);
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

       <div id="thread-form" className={create_classes} >
         <h2>Nieuw draadje</h2>
         <ThreadForm forum={this.props.pk} onCancel={this.showCreate.bind(this, false)}/>
       </div>

       <div id="page-content">
         <table>
           <tbody>
           { _.map(this.state.threads, (thread) => (
              <tr key={thread.pk}>
                <td>
                  <ProfielLink pk={thread.user.pk}>
                    { thread.user.full_name }
                  </ProfielLink>
                  <i>{ moment(thread.laatst_gewijzigd).fromNow() }</i>
                </td>
                <td>
                  <Link to="forum-thread-detail" params={{pk: thread.pk}}>
                    { thread.titel }
                  </Link>
                </td>
                <td>
                  { thread.can_delete
                    ? <button onClick={this.deleteThread.bind(this, thread.pk)} >X</button>
                    : false
                  }
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
