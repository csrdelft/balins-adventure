let forms = require('forms');
let React = require("react");
let _ = require('underscore');
let api = require('api');

class ThreadForm extends React.Component {

  static get propTypes() {
    return { forum: React.PropTypes.number.isRequired };
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
        <div>
          <forms.TextField name="titel" />
          <forms.TextField name="tekst" />
          <forms.SubmitButton />
        </div>
      );
    };

    return <forms.Form formBuilder={formBuilder} onSubmit={handleSubmit} />;
  }
}

module.exports = ThreadForm;
