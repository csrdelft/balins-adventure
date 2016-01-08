import React from "react";
import Reflux from 'reflux';
import $ from "jquery";
import _ from "underscore";

// ui
import Grid from "../components/bootstrap";
import forms from '../components/forms';

// import actions from "auth/actions";

export default class Login extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      error_text: ""
    };
  }

  setError(text) {
    this.setState({
      error_text: text
    });
  }

  submit(data) {
    // simply kick of the login actions
    /*
    actions
      .login(data.username, data.password)
      // and listen for it to complete/fail
      .then(
        (resp) => this.context.router.transitionTo("/"),
        (resp) => this.setError(resp.data.detail)
      );*/

  }

  render() {
    let formBuilder = () => {
      return (
        <Grid.Col id="login" offsetSm={4} sm={4}>
          <Grid.Row id="login-header">
            <h1>Inloggen</h1>
          </Grid.Row>
          {
            this.state.error_text
              ? <p>{this.state.error_text}</p>
              : false
          }
          <forms.CharField name="username" label="Gebruikersnaam" />
          <forms.PasswordField name="password" label="Wachtwoord" />

          <Grid.Row id="login-footer">
            <forms.SubmitButton />
          </Grid.Row>
        </Grid.Col>
      );
    }

    return (
      <Grid.Container>
        <Grid.Row>
          <forms.Form ref="form"
            formBuilder={formBuilder}
            onSubmit={this.submit.bind(this)} />
        </Grid.Row>
      </Grid.Container>
    );
  }
}
