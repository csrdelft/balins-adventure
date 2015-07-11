let { ModernUIForm, validators } = require('form');
var mui = require('material-ui');
var { SelectField } = mui;
let React = require("react");
let _ = require('underscore');

class DraadForm extends ModernUIForm {

  constructor(props) {
    let formfields = {
      titel: {
        type: "string",
        required: true,
        read_only: false,
        label: "Titel",
        validator: validators.compose(
          validators.minLength(15),
          validators.maxLength(255)
        )
      },
      gesloten: {
        type: "boolean",
        required: false,
        read_only: false,
        label: "Gesloten"
      },
      plakkerig: {
        type: "boolean",
        required: false,
        read_only: false,
        label: "Plakkerig",
      }
    };

    super(props, formfields);
  }
}

module.exports = DraadForm;
