var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

class ForumThreadList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      threads: [{
        title: "Initial post"
      }]
    };
  }

  componentDidMount() {
    _.delay(() => {
      this.state.threads.push({
        title: 'Awesome!'
      });
      this.setState(this.state);
    }, 2000);
  }

  render() {
    return <div>
      {
        _.map(this.state.threads,
          (thread, i) => <h3 key={i}>{thread.title}</h3>
        )
      }
      </div>;
  }
}

React.render(<ForumThreadList />, $('#mount-forum-recent')[0]);
