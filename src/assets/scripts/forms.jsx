import React from 'react';
import _ from 'underscore';

import mui, { RaisedButton, Styles } from 'material-ui';

/**
 * Validation functions
 */
export let validators = {
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

export class Form extends React.Component {

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

    this.fields = {};
    this.state = {
      data: {}
    };
  }

  // register a field with the form
  // (this is required for the form to be able to control the children directly)
  register(name, field) {
    if(this.fields[name] !== undefined)
      console.warn(`A field with name ${name} is already registered on this form`);

    this.fields[name] = field;
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

  clear() {
    // clear the children
    _.each(this.fields, (field, name) => field.clear())
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
export class Field extends React.Component {

  static get contextTypes() {
    return { form: React.PropTypes.object.isRequired };
  }

  static get propTypes() {
    return {
      name: React.PropTypes.string.isRequired,
      label: React.PropTypes.string,
      initial: React.PropTypes.any,
      validator: React.PropTypes.func,
    };
  }

  static get defaultProps() {
    return {
      validator: (val) => [],
      label: "",
      initial: undefined
    }
  }

  clear() {
    // clear the value with the initial value
    this.context.form.set(this.props.name, this.props.initial);
  }

  componentWillMount() {
    this.context.form.register(this.props.name, this);

    // init the state
    this.context.form.set(this.props.name, this.props.initial);
  }
}

export class CharField extends Field {

  static get defaultProps() {
    return _.extend(Field.defaultProps, {
      initial: ""
    });
  }

  constructor(props) {
    super(props);

    this.state = {
      error_text: ""
    };
  }

  componentWillMount() {
    super.componentWillMount();

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

export class PasswordField extends CharField {

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

export class InlineTextInput extends React.Component {

  static get propTypes() {
    return {
      label: React.PropTypes.string,
      validator: React.PropTypes.func,
      onChange: React.PropTypes.func.isRequired,
      errorText: React.PropTypes.string
    };
  }

  static get defaultProps() {
    return {
      validator: (val) => [],
      label: "",
      error_text: ""
    };
  }

  constructor(props) {
    super(props);
  }

  onChange() {
    this.props.onChange(this.refs.input.getValue());
  }

  render() {
    return <mui.TextField
            ref="input"
            hintText={this.props.label || this.props.name}
            errorText={this.props.error_text}
            onChange={this.onChange.bind(this)} />;
  }
  
}

export class TextField extends CharField {

  render() {
    return <mui.TextField
      floatingLabelText={this.props.label || this.props.name}
      errorText={this.state.error_text}
      value={this.context.form.get(this.props.name)}
      onChange={this.onChange.bind(this)} fullWidth
      multiLine={true} />;
  }
}

export class SubmitButton extends React.Component {

  static get contextTypes() {
    return { form: React.PropTypes.object.isRequired };
  }

  submitForm() {
    this.context.form.submit();
  }

  render() {
    return <mui.RaisedButton onClick={this.submitForm.bind(this)}>OK</mui.RaisedButton>;
  }
}
