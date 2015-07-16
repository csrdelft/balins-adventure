var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

class Civikaartje extends React.Component {

  constructor(props, context) {
    super(props);
    this.profiel = props.profiel;
    this.context = context;

    this.go = this.go.bind(this)
  }

  go(event) {
    this.context.router.transitionTo('profiel-detail', {uid: this.profiel.uid});
  }

  render() {
    if(this.profiel) {
      return (
       <div className='civikaartje'>
         <a onClick={this.go}>{this.profiel.full_name} ({this.profiel.uid})</a>
         <p>{this.profiel.adres}</p>
         <p>{this.profiel.postcode} {this.profiel.woonplaats}</p>
         <p>{this.profiel.mobiel}</p>
       </div>
      );
    } else {
      return <p>Loading...</p>;
    }
  }

}

Civikaartje.contextTypes = {
  router: React.PropTypes.func
};

module.exports = Civikaartje;
