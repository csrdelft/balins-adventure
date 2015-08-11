let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let PropTypes = require('react-router').PropTypes;
let api = require("api")

let Civikaartje = require("./Civikaartje");
let {Link} = require('react-router');

class LidPhoto extends React.Component {

  static get propTypes() {
    return {
      pk: React.PropTypes.string.isRequired,
      name: React.PropTypes.string
    };
  }

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    };
  }

  constructor(props, context) {
    super(props, context);
  }

  render() {
    return (
      <div className="lid-photo">
        <Link
           to="profiel-detail"
           params={{pk: this.props.pk}}
        >
          <img src={api.photo_url(this.props.pk)} />
        </Link>
      </div>
    );
  }
}

module.exports = LidPhoto;
