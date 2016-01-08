import React from "react";
import $ from "jquery";
import _ from "underscore";
import api from "api";
import moment from 'moment';

export default class ForumThreadList extends React.Component {
  static get propTypes() {
    return {
      threads: React.PropTypes.array.isRequired
    };
  }

  render() {
    return ( <table>
      <tbody>
        {
          _.map(this.props.threads, (thread) => (
            <tr key={thread.pk}>k
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
                {
                  thread.can_delete
                  ? <button onClick={this.deleteThread.bind(this, thread.pk)} >X</button>
                  : false
                }
              </td>
            </tr>
          ))
        }
      </tbody>
    </table> );
  }
}
