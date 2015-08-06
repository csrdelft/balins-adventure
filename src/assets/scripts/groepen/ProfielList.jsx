let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let actions = require("./actions");
let stores = require("./stores");
let forms = require('forms');

// view stuff
let { Link, RouteHandler } = require('react-router');
let Layout = require("Layout");

class ProfielList extends React.Component {

  static get propTypes() {
    // string because it's a route parameter
    return {page: React.PropTypes.string.isRequired };
  }

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    };
  }

  constructor(props) {
    super(props);

    this.search_text = "";
    this.filters = {};

    this.state = {
      profielen: [],
      search_profielen: [],
      searching: false
    };
  }

  componentWillMount() {
    // listen to updates to the profielen list store
    stores.profielListStore
      .listen((profielen) => this.setState({profielen: profielen}));

    // kick of initial load
    actions.loadProfielen(this.props.page);
  }

  componentWillReceiveProps(nextProps) {
    if(nextProps.page != this.props.page) {
      // load the next page
      actions.loadProfielen(nextProps.page);
    }
  }

  search(search_text) {
    this.search_text = search_text;
    this.do_search(this.search_text, this.filters);
  }

  filter(name, value) {
    if(value == "") {
      delete this.filters[name];
    } else {
      this.filters[name] = value;
    }

    this.do_search(this.search_text, this.filters);
  }

  do_search(search_text, filters) {
    if(search_text === "" && filters === {}) {
      // go back to usual paged mode
      this.setState({
        searching: false,
        search_profielen: []
      });
    } else {
      // conduct the search
      actions
        .searchProfielen(search_text, filters)
        .then((resp) => {
          this.setState({
            searching: true,
            search_profielen: resp.data.results
          });
        })
        .done();
    }
  }

  render() {
    let profielen;
    if(this.state.searching)
      profielen = this.state.search_profielen;
    else
      profielen = this.state.profielen[this.props.page];

    return (
      <Layout title="Leden Lijst">
        <div id="profiel-list">
          <div id="page-action-menu">
            <ul>
              <li className="action-input">
                <forms.InlineTextInput
                  label="zoeken..."
                  onChange={_.debounce(this.search, 1000).bind(this)}/>
              </li>
              <li className="action-input">
                <forms.InlineTextInput
                  label="lichting..."
                  onChange={_.debounce(this.filter, 1000).bind(this, "lichting")}/>
              </li>
            </ul>
          </div>
          <div id="profiel-table">
            <table className="table table-bordered table-striped" id="profiel-list">
              <thead>
                <tr>
                  <th>Lidno.</th>
                  <th>Naam</th>
                  <th>E-mail</th>
                </tr>
              </thead>
              <tbody>
                { _.map(profielen, (profiel) => (
                    <tr>
                      <td>{profiel.pk}</td>
                      <td>
                          <Link to="profiel-detail" params={{pk: profiel.pk}}>{profiel.full_name}</Link>
                      </td>
                      <td>{profiel.email}</td>
                    </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </Layout>
    );
  }
};

module.exports = ProfielList;
