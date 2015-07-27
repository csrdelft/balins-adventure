let forms = require('forms');
let React = require("react");
let _ = require('underscore');
let api = require('api');
let mui = require("material-ui");

class ThreadForm extends React.Component {

  static get propTypes() {
    return {
      forum: React.PropTypes.number.isRequired,
      onCancel: React.PropTypes.func
    };
  };

  constructor(props) {
    super(props);
  }

  render() {
    let handleSubmit = (data) => {
      // create the request body
      data = _.extend(data, {
        forum: this.props.forum,
        gesloten: false
      });

      // post the forum thread
      // and return the promise
      return api.forum.threads.create(data).then(
        // todo
        (resp) => console.log("SUCCESS!", resp),
        (resp) => _.each(resp.data, (errs, name) => this.set_error(name, errs[0]))
      );
    }

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

    return <forms.Form formBuilder={formBuilder} onSubmit={handleSubmit} />;
  }
}

module.exports = ThreadForm;
