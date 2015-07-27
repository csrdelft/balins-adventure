let React = require("react");
let _ = require('underscore');
let api = require('api');
let mui = require("material-ui");
let forms = require('forms');
let actions = require('forum/actions');

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
      data = _.extend(data, {
        forum: this.props.forum,
        gesloten: false
      });

      // kick of the create actions
      // TODO error handling
      actions
        .create(data)
        .catch((resp) => console.error(resp.data))
        .done();
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
