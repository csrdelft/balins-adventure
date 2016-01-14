import React from "react";
import _ from 'underscore';
import api from '../utils/api';
import mui from "material-ui";
import * as forms from './forms';
import actions from '../actions';

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

      // TODO
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
