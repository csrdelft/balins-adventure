var React = require("react");
var $ = require("jquery");
var _ = require("underscore");
var api = require("api");

class ForumThreadList extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      threads: []
    };
  }

  update() {
    api.forum.get_recent()
      .then(
        (resp) => this.setState({ threads: resp.data }),
        (resp) => console.error('Getting recent forum posts failed with status ' + resp.status)
      );
  }

  componentDidMount() {
    // load initial recent forum posts
    this.update();

    // set the regular update
    window.setInterval(() => this.update(), this.props.updateInterval);
  }

  render() {
    return <div>
      {
        _.map(this.state.threads,
          (thread, i) => <h3 key={i}>{thread.titel}</h3>
        )
      }
      </div>;
  }
}

ForumThreadList.propTypes = { updateInterval: React.PropTypes.number };
ForumThreadList.defaultProps = { updateInterval: 10000 };

// initiate the forum recent threads list
var forum_recent = <ForumThreadList />

React.render(forum_recent, $('#mount-forum-recent')[0]);
