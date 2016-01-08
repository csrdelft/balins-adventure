import React from "react";
import $ from "jquery";
import _ from "underscore";
import api from "../utils/api";
import { Link } from 'react-router';

class Civikaartje extends React.Component {

  static get propTypes() {
    return {
      pk: React.PropTypes.string.isRequired,
      name: React.PropTypes.string
    };
  }

  constructor(props) {
    super(props);
    this.pk = props.pk;

    this.state = {
      profiel: undefined
    };
  }

   update(pk) {
    api.profiel.get(pk)
      .then(
      (resp) => this.setState({profiel: resp.data}),
      (resp) => console.error('Getting profiel failed with status ' + resp.status)
    );
  }

	componentWillMount() {
    this.update(this.pk);
  }

  componentWillReceiveProps(nextProps) {
    if(this.pk != nextProps.pk) {
      this.update(nextProps.pk);
    }
  }

  render() {
    if(this.state.profiel) {
      return (
       <div className='civikaartje'>
         <Link to="profiel-detail" params={{pk: this.state.profiel.pk}}>{this.state.profiel.full_name} ({this.state.profiel.pk})</Link>
         <p>{this.state.profiel.adres}</p>
         <p>{this.state.profiel.postcode} {this.state.profiel.woonplaats}</p>
         <p>{this.state.profiel.mobiel}</p>
       </div>
      );
    } else {
      return <div>Loading... Civikaartje</div>;
    }
  }
}

module.exports = Civikaartje;
