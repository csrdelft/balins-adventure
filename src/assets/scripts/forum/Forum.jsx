let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let { Link, RouteHandler } = require('react-router');
let api = require("api");

let Layout = require("Layout");

class ForumSideMenu extends React.Component {

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    }
  }

  constructor(props, context) {
    super(props, context);

    this.state = {
      fora: []
    };
  }

  update() {
    api.forum.list()
      .then(
        (resp) => this.setState({fora: resp.data}),
        (resp) => console.error("Failed to get sub fora with status " + resp.status)
      );
  }

  componentWillMount() {
    this.update();
  }

  render() {

    return (
      <ul>
        {
          _.map(this.state.fora, (forum) => {
            return (
              <li key={forum.pk}>
                <Link to="forum-thread-list" params={{pk: forum.pk}}>
                {forum.titel}
                </Link>
              </li>
            );
          })
        }
      </ul>
    );
  }
}

class Forum extends React.Component {
  render() {
    return (
      <Layout title="Reformaforum" sidemenu={ForumSideMenu}>
        <RouteHandler {...this.props.params} />
      </Layout>
    );
  }
}

module.exports = Forum;
