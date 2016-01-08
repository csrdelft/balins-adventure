let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let mui = require("modern-ui");

class Loading extends React.Component {
  render() {
    return <mui.RefreshIndicator size={40} status="loading" />;
  }
}
module.exports = Loading; 
