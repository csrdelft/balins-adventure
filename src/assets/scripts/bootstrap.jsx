let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let cs = require("classnames");

class Container extends React.Component {
  render() {
    return <div {...this.props} className="container">{this.props.children}</div>;
  }
}

class Row extends React.Component {
  render() {
    return <div {...this.props} className="row">{this.props.children}</div>;
  }
}

class Col extends React.Component {
  render() {
    let classnames = cs({
      [`col-xs-${this.props.xs}`]: this.props.xs,
      [`col-sm-${this.props.sm}`]: this.props.sm,
      [`col-md-${this.props.md}`]: this.props.md,
      [`col-lg-${this.props.lg}`]: this.props.lg,
      [`col-xs-offset-${this.props.offsetXs}`]: this.props.offsetXs,
      [`col-sm-offset-${this.props.offsetSm}`]: this.props.offsetSm,
      [`col-md-offset-${this.props.offsetMd}`]: this.props.offsetMd,
      [`col-lg-offset-${this.props.offsetLg}`]: this.props.offsetLg,
    });
    return <div {...this.props} className={classnames}>{this.props.children}</div>;
  }
}

module.exports = {
  Container: Container,
  Row: Row,
  Col: Col
};
