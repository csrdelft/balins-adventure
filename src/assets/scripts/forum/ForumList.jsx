
let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let api = require("api");

let { Table, Column } = require('fixed-data-table');
let PostForm = require("forum/PostForm");

class ForumList extends React.Component {

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      threads: []
    };
  }

  update() {
    // use the api to get most recent forum threads
    // this returns a promise that we can register our success and error callbacks on
    // at success we simply update the state of the component
    api.forum.threads.get_recent()
      .then(
        (resp) => this.setState({ threads: resp.data }),
        (resp) => console.error('Getting recent forum posts failed with status ' + resp.status)
      );
  }

  componentDidMount() {
    // load initial recent forum posts
    this.update();
  }

  render() {
    return (
      <div>
        <div id="page-action-menu">
          <ul>
            <li>
              <button className="action">
                + draadje
              </button>
            </li>
          </ul>
        </div>

        <div>
          <table>
            <thead>
              <th>Auteur</th>
              <th>Titel</th>
            </thead>
            <tbody>
              { _.map(this.state.threads, (thread) =>
                  <tr key={thread.pk}>
                    <td>{thread.user.full_name}</td>
                    <td>{thread.titel}</td>
                  </tr>
                )
              }
            </tbody>
          </table>
        </div>
      </div>
    );
  }
}

module.exports = ForumList;
