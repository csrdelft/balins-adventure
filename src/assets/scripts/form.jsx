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

class ModernUIForm extends React.Component {

  static get childContextTypes() {
    return { muiTheme: React.PropTypes.object }
  }

  static get propTypes() {
    return { fields: React.PropTypes.object }
  }

  static get defaultProps() {
    return { fields: {} }
  }

  getChildContext() {
    return {
      // set the mui theme on the children through the context
      muiTheme: Styles.ThemeManager().getCurrentTheme()
    };
  }

  /**
   * `fields` is an object that describes the form
   *
   * form_fields = {
   *   fieldname: {
   *     type: string (integer|string|boolean)
   *     label: string
   *     read_only: bool
   *     required: bool
   *     widget: string (a name in the material-ui module)
   *   }
   * }
   */
  constructor(props, fields, initial_values={}) {
    super(props);
    this.fields = _.extend(props.fields, fields);
    this.state = {
      // set default error to empty string
      error_text:
        _.mapObject(this.fields, (v, k) => ""),
      values:
        _ .chain(this.fields)
          .mapObject((v, k) => undefined)
          .extend(initial_values)
          .value()
    };
  }

  /**
   * Set the error text for the field named name
   */
  set_error(name, error_text) {
    this.setState({
      error_text: _.extend(this.state.error_text, {
        [ name ]: error_text
      })
    });
  }

  /**
   * Convert the field specification into a React component value.
   */
  field_to_widget(name, field) {
    let props = _.extend(field.widget_props || {}, {
      floatingLabelText: field.label,
      label: field.label,
      errorText: this.state.error_text[name],
      value: this.state.values[name],
      onChange: ((e) => {
        let val = e.target.value;

        // update the state
        this.setState({
          values: _.extend(this.state.values, {
            [ name ]: val
          })
        });

        // validation
        if(field.validator) {
          // call validator
          let errors = field.validator(val);
          this.set_error(name, _.first(errors) || "");

          // call custom handlers
          let handler = this[`handle_${name}_change`];
          if(handler) {
            handler.bind(this)(e);
          }
        }
      }).bind(this)
    });

    if(field.widget) {
      // dynamically crate the react component using a factory
      // (basically desugared jsx)
      return React.createFactory(mui[field.widget])(props);
    } else if(field.type == 'string') {
      return <mui.TextField {...props} fullWidth />
    } else if(field.type == 'boolean') {
      return <mui.Checkbox {...props} label={field.label}/>;
    } else if(field.type == 'integer') {
      return <mui.TextField {...props} floatingLabelText={field.label}/>;
    }

    throw Error(`Unknown field type: ${field.type}`);
  }

  render() {
    return (
      <form>
        {
          _ .chain(this.fields)
            .pick((field, name) => !field.read_only)
            .map((field, name) =>
              <div key={name}>
                { this.field_to_widget(name, field) }
              </div>
            )
            .value()
        }
      </form>
    );
  }
}

module.exports = {
  ModernUIForm: ModernUIForm,
  validators: validators
};
