let React = require("react");
let _ = require('underscore');
let api = require('api');
let mui = require("material-ui");
let forms = require('forms');
let actions = require('forum/actions');

class PostForm extends React.Component {

  static get propTypes() {
    return {
      thread: React.PropTypes.string.isRequired,
      threadPage: React.PropTypes.string.isRequired
    };
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
        .catch((resp) => console.error(resp.data))
        .then(() =>
          // clear the form to prevent resubmit
          this.refs.postForm.clear()
        )
        .done();
    };

    let formBuilder = () => {
      return (
        <div className="forumpost-form">
          <forms.TextField name="tekst" />
          <br />
          <forms.SubmitButton />
        </div>
      );
    };

    return <forms.Form ref="postForm" formBuilder={formBuilder} onSubmit={handleSubmit} />;
  }
}

module.exports = PostForm;
