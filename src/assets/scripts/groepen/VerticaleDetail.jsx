import React from 'react';
import { Link } from 'react-router';
import _ from "underscore";
import actions from "./actions";
import stores from "./stores";
import bs from "bootstrap";
import Layout from "Layout";
import LidPhoto from "groepen/LidPhoto";

export default class VerticaleDetail extends React.Component {

  static get propTypes() {
    return {pk: React.PropTypes.string.isRequired};
  }

  constructor(props) {
    super(props);

    this.state = {
      verticale: undefined
    };
  }

  componentWillMount() {
    actions.loadVerticale(this.props.pk);
  }

  componentDidMount() {
    this.setState({verticale: stores.verticaleDetailStore.get(this.props.pk)});
    this.unsubscribe = stores.verticaleDetailStore.listen((verticalen) => this.setState({
      verticale: stores.verticaleDetailStore.get(this.props.pk)
    }));
  }

  componentWillUnmount() {
    this.unsubscribe();
  }

  render_leden() {
    let by_year = _.groupBy(this.state.verticale.leden, (lid) => lid.user.lidjaar);
    let years = _(by_year).chain()
      .keys()
      .sortBy((year) => year)
      .value();

    return <div id="verticale-detail">
      { _.map(years, (year) =>
        <div key={year} className="year">
          <h2>{year}</h2>
          <div className="leden">
          { _.map(by_year[year], (lid) =>
            <LidPhoto key={lid.user.pk} pk={lid.user.pk} name={lid.user.full_name} />
          )}
          </div>
        </div>
      )}
    </div>;
  }

  render() {
    let v = this.state.verticale;
    return <Layout title={v ? v.naam : "Verticale..."}>
      {
        v
        ? this.render_leden()
        : <h2>Loading...</h2>
      }
    </Layout>;
  }
}
