var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

class InlineInput extends React.Component {

  constructor(props) {
    super(props);

    this.value = this.props.value;
    this.setter = this.props.setter;

    this.state = {
      editing: false
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleFocus = this.handleFocus.bind(this);
    this.handleBlur = this.handleBlur.bind(this);
  }

  handleChange(event) {
    this.setter(event.target.value);
    this.value = event.target.value;
  }

  handleFocus(event) {
    this.setState({editing: true});
  }

  handleBlur(event) {
    this.setState({editing: false});
  }

  render() {
    if(this.state.editing) {
      return <input type="text"
        defaultValue={this.value}
        onChange={this.handleChange}
        onBlur={this.handleBlur}
        autoFocus />;
    } else {
      return <span onDoubleClick={this.handleFocus} >{this.value}</span>;
    }
  }
}

module.exports = InlineInput;
