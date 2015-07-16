var React = require("react");
var $ = require("jquery");
var _ = require("underscore");
var api = require("api");

var PropTypes = require('react-router').PropTypes;

class MededelingList extends React.Component {


  constructor(props, context) {
    super(props);

    this.context = context;
  }

  go(event) {
    let pk = $(event.target).data('pk');
    this.context.router.transitionTo("mededeling-detail", {pk: pk});
  }

  render() {
    return <div>
      <h1>Mededelingen</h1>
      <ul>
        {
          _.map(this.props.mededelingen, (mededeling, i) =>
            <li key={mededeling.pk}>
              <a data-pk={mededeling.pk} onClick={this.go.bind(this)}>{mededeling.titel}</a>
            </li>
          )
        }
      </ul>
    </div>;
  }
}

MededelingList.contextTypes = {
  router: React.PropTypes.func.isRequired
};

// the component takes an attribute to manipulate the update interval
MededelingList.propTypes = {
  mededelingen: React.PropTypes.arrayOf(React.PropTypes.object).isRequired
};

module.exports = MededelingList;
