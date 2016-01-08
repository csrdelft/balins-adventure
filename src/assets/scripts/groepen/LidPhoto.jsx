let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let api = require("api");

let Civikaartje = require("./Civikaartje");
let {Link} = require('react-router');

class LidPhoto extends React.Component {

  static get propTypes() {
    return {
      pk: React.PropTypes.string.isRequired,
      name: React.PropTypes.string,
      size: React.PropTypes.string
    };
  }

  static get defaultProps() {
    return {
      size: 'md',
      name: ''
    };
  }

  render() {
    return (
      <div className={`lid-photo ${this.props.size}`}>
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
