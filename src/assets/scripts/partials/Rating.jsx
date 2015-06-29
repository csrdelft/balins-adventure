var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

class RatingField extends React.Component {
  constructor(props) {
    super(props);

    // initial state
    this.state = {
      rating: 0
    };

    // bind the handlers to this object,
    // so they can be used as event handlers
    this.handleClick = this.handleClick.bind(this);
  }

  // setters
  rate(i) {
    this.setState({
      rating: i
    });
  }

  // handlers
  handleClick(e) {
    this.rate($(e.target).data('value'));
  }

  render() {
    var curRating = this.state.rating;
    return (
      <div>
        {
          _.map(
            _.range(1, Math.min(curRating, this.props.max) + 1),
            (i) => <i data-value={i} onClick={this.handleClick}>X</i>
          )
        }
        {
          _.map(
            _.range(1, Math.max(this.props.max - curRating, 0) + 1),
            (i) => <i data-value={curRating + i} onClick={this.handleClick}>O</i>
          )
        }
      </div>
    );
  }
}

RatingField.propTypes = { max: React.PropTypes.number };
RatingField.defaultProps = { max: 5 };

module.exports = RatingField;
