var React = require("react");
var $ = require("jquery");
var _ = require("underscore");

let Link = require('react-router');

class Civikaartje extends React.Component {

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    }
  }

  constructor(props, context) {
    super(props, context);
    this.profiel = props.profiel;

  }

  render() {
    if(this.profiel) {
      return (
       <div className='civikaartje'>
         <Link to="profiel-detail" params={{pk: this.profiel.pk}}>{this.profiel.full_name} ({this.profiel.pk})</Link>
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

module.exports = Civikaartje;
