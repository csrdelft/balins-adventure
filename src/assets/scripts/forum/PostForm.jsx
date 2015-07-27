let React = require("react");
let _ = require('underscore');
let api = require('api');
let mui = require("material-ui");
let forms = require('forms');
let actions = require('forum/actions');

class PostForm extends React.Component {

  static get propTypes() {
    return {
      thread: React.PropTypes.number.isRequired
    };
  }

  clear() {
    console.debug("TODO: Supposed to clear the form now...");
  }

  render() {
    let handleSubmit = (data) => {
      data = _.extend(data, {
        draad: this.props.thread
      });

      // kick of the create actions
      // TODO error handling
      actions
        .createPost(data)
        .then(() => this.clear())
        .catch((resp) => console.error(resp.data))
        .done();
    }

    let formBuilder = () => {
      return (
        <div className="forumpost-form">
          <forms.TextField ref="form" name="tekst" />
          <br />
          <forms.SubmitButton />
        </div>
      );
    };

    return <forms.Form formBuilder={formBuilder} onSubmit={handleSubmit} />;
  }
}

module.exports = PostForm;
