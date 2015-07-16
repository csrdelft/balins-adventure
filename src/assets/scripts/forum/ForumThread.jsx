let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let Layout = require("Layout");

let api = require("api");

class ForumThread extends React.Component {

  static get propTypes() {
    return { pk: React.PropTypes.string.isRequired };
  }

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      thread: undefined
    };
  }

  update(pk) {
    api.forum.threads.get(pk)
      .then(
      (resp) => this.setState({thread: resp.data}),
      (resp) => console.error('Getting thread failed with status ' + resp.status)
    );
  }

  componentWillReceiveProps(nextProps) {
    if(this.props.pk != nextProps.pk) {
      this.update(nextProps.pk);
    }
  }

  componentWillMount() {
    this.update(this.props.pk);
  }

  render() {
    if(this.state.thread)
      return <ul>
        {_.map(this.state.thread.posts, (p) => {
          return <li>{p.tekst}</li>;
        })}
      </ul>;
    else
      return <h1>Loading...</h1>;
  }
}

module.exports = ForumThread;

