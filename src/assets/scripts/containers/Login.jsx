import React from "react";
import $ from "jquery";
import _ from "underscore";
import * as actions from '../actions';
import { connect } from 'react-redux';

// ui
import * as Grid from "../components/bootstrap";
import * as forms from '../components/forms';

class Login extends React.Component {

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
    this.props.dispatch(actions
      .auth
      .login(data.username, data.password))
      .then(
        (resp) => console.log("DONE!"),
        (resp) => this.setError(resp.data.detail)
      );
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

export default connect(function(state){return {}})(Login);
