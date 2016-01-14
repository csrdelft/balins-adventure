import React from "react";
import _ from 'underscore';
import * as forms from '../components/forms';
import * as actions from '../actions';

export default class PostForm extends React.Component {

  static get propTypes() {
    return {
      draadje: React.PropTypes.number.isRequired
    };
  }

  render() {
    let handleSubmit = (data) => {
      data = _.extend(data, {
        draadje: this.props.draadje
      });

      // kick of the create actions
      // TODO
      /*actions
        .createPost(data)
        .catch((resp) => console.error(resp.data))
        .then(() =>
          // clear the form to prevent resubmit
          this.refs.postForm.clear()
        )
        .done();*/
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
