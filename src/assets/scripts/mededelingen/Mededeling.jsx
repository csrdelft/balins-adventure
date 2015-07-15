var React = require("react");
var $ = require("jquery");
var _ = require("underscore");
var api = require("api");

var ProfielLink = require('../groepen/ProfielLink')

class Mededeling extends React.Component {
  constructor(props) {
    super(props);

    // initial state
    this.state = {
      mededeling: undefined
    };
  }

  update() {
    api.mededelingen.get_mededeling(this.props.params.id)
      .then(
      (resp) => this.setState({mededeling: resp.data}),
      (resp) => console.error('Getting mededeling failed with status ' + resp.status)
    );
  }

  componentWillMount() {
    // load initial recent forum posts
    this.update();
  }

 render() {
    var mededeling = this.state.mededeling;
    if(mededeling) {
      return (
       <div>
         <h1>{mededeling.titel}</h1>
         <ProfielLink uid={mededeling.user}/>
         <p>{mededeling.tekst}</p>
       </div>
      );
    } else{
      return (<span></span>);
    }
  }
}

module.exports = Mededeling;
