import React from "react";
import _ from 'underscore';
import api from 'api';
import mui from "material-ui";
import forms from 'forms';
import actions from 'forum/actions';

export default class ThreadForm extends React.Component {

  static get propTypes() {
    return {
      forum: React.PropTypes.string.isRequired,
      onCancel: React.PropTypes.func
    };
  }

  render() {
    let handleSubmit = (data) => {
      data = _.extend(data, {
        forum: this.props.forum,
        gesloten: false
      });

      // kick of the create actions
      // TODO error handling
      actions
        .createThread(data)
        .catch((resp) => console.error(resp.data))
        .then(() => this.refs.form.clear())
        .done();
    };

    let formBuilder = () => {
      return (
        <div className="thread-form">
          <forms.CharField name="titel" />
          <br />
          <forms.TextField name="tekst" />
          <br />
          {
            this.props.onCancel
            ? <mui.RaisedButton onClick={this.props.onCancel}>Annuleren</mui.RaisedButton>
            : false
          }
          <forms.SubmitButton />
        </div>
      );
    };

    return <forms.Form ref="form" formBuilder={formBuilder} onSubmit={handleSubmit} />;
  }
}
