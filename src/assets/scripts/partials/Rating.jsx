import React from "react";
import $ from "jquery";
import _ from "underscore";

export default class RatingField extends React.Component {

  static get propTypes() { return { max: React.PropTypes.number };}

  static get defaultProps() { return { max: 5 };}

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
