var React = require('react');
var _ = require('underscore');

var mui = require('material-ui');
var { RaisedButton, Styles } = mui;
window.Styles = Styles;

class ModernUIForm extends React.Component {

  static get childContextTypes() {
    return { muiTheme: React.PropTypes.object }
  }

  static get propTypes() {
    return { fields: React.PropTypes.object }
  }

  static get getDefaultProps() {
    return { fields: [] }
  }

  /**
   * Where form fields is an object that describes the form
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
  constructor(props) {
    super(props);
    this.fields = props.fields;
    this.state = {
      // set default error to empty string
      error_text: _.mapObject(this.fields, (v, k) => "")
    };
  }

  getChildContext() {
    return {
      // set the mui theme on the children through the context
      muiTheme: Styles.ThemeManager().getCurrentTheme()
    };
  }

  field_to_widget(name, field) {
    if(field.widget) {
      // dynamically crate the react component using a factory
      // (basically desugared jsx)
      return React.createFactory(mui[field.widget])(_.extend(field.widget_props, {
        floatingLabelText: field.label,
        label: field.label
      }));
    } else if(field.type == 'string') {
      return <mui.TextField
        {...field.widget_props}
        fullWidth
        errorText={this.state.error_text[name]}
        floatingLabelText={field.label}/>;
    } else if(field.type == 'boolean') {
      return <mui.Checkbox {...field.widget_props} label={field.label}/>;
    } else if(field.type == 'integer') {
      return <mui.TextField {...field.widget_props} floatingLabelText={field.label}/>;
    }

    throw Error(`Unknown field type: ${field.type}`);
  }

  render() {
    return (
      <form>
        {
          _ .chain(this.fields)
            .filter((f) => !f.read_only)
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
  ModernUIForm: ModernUIForm
};
