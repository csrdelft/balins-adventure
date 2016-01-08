let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let api = require("api");

let ProfielLink = require('../groepen/ProfielLink');

class MededelingDetail extends React.Component {

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
    if(this.props.params.pk != nextProps.params.pk) {
      this.update(nextProps.params.pk);
    }
  }

  componentWillMount() {
    this.update(this.props.params.pk);
  }

  render() {
    let mededeling = this.state.mededeling;
    if(mededeling) {
      return <div>
        <h1>{mededeling.titel}</h1>
        <ProfielLink pk={mededeling.user.pk}>{mededeling.user.full_name}</ProfielLink>
        <p>{mededeling.tekst}</p>
      </div>;
    } else {
      return <p>Loading... MededelingDetail</p>;
    }
  }
}

module.exports = MededelingDetail;
