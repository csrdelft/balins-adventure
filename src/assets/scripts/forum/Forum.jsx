let React = require("react");
let $ = require("jquery");
let _ = require("underscore");
let { Link, RouteHandler } = require('react-router');
let api = require("api");

let Layout = require("Layout");
let mui = require('material-ui');
let { List, ListItem } = mui;

class ForumSideMenu extends React.Component {

  static get contextTypes() {
    return {
      router: React.PropTypes.func.isRequired
    }
  }

  constructor(props, context) {
    super(props, context);

    this.state = {
      fora: [],
      // defaults to open
      categories_open: {}
    };
  }

  update() {

    api.forum.list()
      .then(
        (resp) => {
          let grouped_fora = _(resp.data)
              .groupBy((forum) => forum.categorie.pk);
          let categories = _(grouped_fora).map((fora) => fora[0].categorie);
          this.setState({fora: grouped_fora, categories: categories});
        },
        (resp) => console.error("Failed to get sub fora with status " + resp.status)
      );
  }

  componentWillMount() {
    this.update();
  }

  goTo(forum_pk) {
    this.context.router.transitionTo("forum-thread-list", {pk: forum_pk});
  }

  render() {
    return (
      <List>
        {
          _.map(this.state.fora, (fora, cat_pk) =>
            <ListItem
                key={cat_pk}
                primaryText={this.state.categories[cat_pk].titel}
                open={true}
                >
              {
                _.map(fora, (forum) => 
                   <ListItem
                      key={forum.pk}
                      onClick={this.goTo.bind(this, forum.pk)}
                      primaryText={forum.titel} />
                )
              }
            </ListItem>
          )
        }
      </List>
    );
  }
}

class Forum extends React.Component {
  render() {
    return (
      <Layout title="Reformaforum" sidemenu={ForumSideMenu}>
        <RouteHandler {...this.props.params} />
      </Layout>
    );
  }
}

module.exports = Forum;
