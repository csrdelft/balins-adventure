let React = require('react');
let _ = require('underscore');

let mui = require('material-ui');
let { RaisedButton, Styles } = mui;

/**
 * Validation functions
 */
let validators = {
  /* Composes all passed validators into a single validator
   */
  compose(...validators) {
    return (val) => {
      return _ .chain(validators)
        .map((validator) => validator(val))
        .flatten()
        .value();
    };
  },

  /* Checks that val has minimum length `min`
   */
  minLength: (min) => (val) => {
    if(val.trim().length < min) {
      return [`Moet minstens ${min} tekens bevatten`];
    } else {
      return [];
    }
  },

  /* Checks that val has maximum length `max`
   */
  maxLength: (max) => (val) => {
    if(val.trim().length > max) {
      return [`Mag maximaal ${max} tekens bevatten`];
    } else {
      return [];
    }
  }
};

class Form extends React.Component {

  static get propTypes() {
    return {
      formBuilder: React.PropTypes.func.isRequired,
      onSubmit: React.PropTypes.func.isRequired
    };
  }

  static get childContextTypes() {
    return {
      form: React.PropTypes.object.isRequired
    };
  }

  constructor(props) {
    super(props);

    this.state = {
      data: {}
    };
  }

  set(name, value) {
    this.setState({
      data: _.extend(this.state.data, { [name]: value })
    });
  }

  get(name) {
    return this.state.data[name];
  }

  getChildContext() {
    return {
      form: this
    };
  }

  submit() {
    this.props.onSubmit(this.state.data);
  }

  render() {
    // we use a formBuilder here because React 0.13.3
    // uses the context as set by the 'owner', not parent, of an element
    // since the owner is not the Form if we use this.props.children,
    // we have to delay initialization of the children till here
    return <form>{this.props.formBuilder()}</form>;
  }
}

/**
 * Abstract over some boilerplate that is common in all fields of a form.
 */
class Field extends React.Component {

  static get contextTypes() {
    return { form: React.PropTypes.object.isRequired };
  }

  static get propTypes() {
    return {
      name: React.PropTypes.string.isRequired,
      label: React.PropTypes.string,
      validator: React.PropTypes.func,
    };
  }

  static get defaultProps() {
    return {
      validator: (val) => [],
      label: ""
    }
  }
}

class TextField extends Field {

  constructor(props) {
    super(props);

    this.state = {
      error_text: ""
    };
  }

  componentWillMount() {
    // initial value
    this.context.form.set(this.props.name, "");
  }

  /**
   * Set the error text for the field named name
   */
  set_error(error_text) {
    this.setState({
      error_text: error_text
    });
  }

  onChange(e) {
    // validate and set error text
    let errors = this.props.validator(e.target.value);
    this.set_error(name, _.first(errors) || "");

    // update the form data
    this.context.form.set(this.props.name, e.target.value);
  }

  render() {
    return <mui.TextField
      floatingLabelText={this.props.label || this.props.name}
      errorText={this.state.error_text}
      value={this.context.form.get(this.props.name)}
      onChange={this.onChange.bind(this)} fullWidth />;
  }
}

class PasswordField extends TextField {

  render() {
    return <mui.TextField
      floatingLabelText={this.props.label || this.props.name}
      errorText={this.state.error_text}
      value={this.context.form.get(this.props.name)}
      onChange={this.onChange.bind(this)} fullWidth >
      <input type="password"/>
    </mui.TextField>;
  }
}

class SubmitButton extends Field {

  submitForm() {
    this.context.form.submit();
  }

  render() {
    return <mui.RaisedButton onClick={this.submitForm.bind(this)}>OK</mui.RaisedButton>;
  }
}

module.exports = {
  Form: Form,
  Field: Field,
  TextField: TextField,
  SubmitButton: SubmitButton,
  PasswordField: PasswordField,
  validators: validators
};
