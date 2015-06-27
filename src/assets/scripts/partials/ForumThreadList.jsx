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

    this.interval = null;
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
    this.interval = window.setInterval(() => this.update(), this.props.updateInterval);
  }

  componentWillUnmount() {
    window.clearInterval(this.interval);
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
ForumThreadList.defaultProps = { updateInterval: 60000 };

module.exports = ForumThreadList
