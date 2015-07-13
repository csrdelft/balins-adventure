let { ModernUIForm, validators } = require('form');
var mui = require('material-ui');
var { SelectField } = mui;
let React = require("react");
let _ = require('underscore');
let api = require('api');

class DraadForm extends ModernUIForm {

  static get propTypes() {
    return { forum: React.PropTypes.number.isRequired };
  };

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

    // forum part pk
    this.forum = props.forum;
  }

  handleSubmit() {
    // create the request body
    let data = _.extend(this.state.values, {
      forum: this.forum
    });

    // post the forum thread
    api.forum.threads.create(data).then(
      // todo
      (resp) => console.log("SUCCESS!", resp),
      (resp) => _.each(resp.data, (errs, name) => this.set_error(name, errs[0]))
    );
  }
}

module.exports = DraadForm;
