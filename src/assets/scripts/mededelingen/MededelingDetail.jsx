let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let api = require("api");

let ProfielLink = require('../groepen/ProfielLink')

class MededelingDetail extends React.Component {

  static get propTypes() {
    return {
      pk: React.PropTypes.string.isRequired
    }
  }

  constructor(props) {
    super(props);

    // initial state
    this.state = {
      mededeling: undefined
    };
  }

  update(pk) {
    api.mededelingen.get(pk)
      .then(
      (resp) => this.setState({mededeling: resp.data}),
      (resp) => console.error('Getting mededeling failed with status ' + resp.status)
    );
  }

  componentWillReceiveProps(nextProps) {
    if(this.props.pk != nextProps.pk) {
      this.update(nextProps.pk);
    }
  }

  componentWillMount() {
    this.update(this.props.pk);
  }

  render() {
    let mededeling = this.state.mededeling;
    if(mededeling) {
      return <div>
        <h1>{mededeling.titel}</h1>
        <ProfielLink uid={parseInt(mededeling.user)} />
        <p>{mededeling.tekst}</p>
      </div>;
    } else {
      return <p>Loading</p>;
    }
  }
}

module.exports = MededelingDetail;
