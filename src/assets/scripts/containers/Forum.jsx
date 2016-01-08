import React from "react";
import $ from "jquery";
import _ from "underscore";
import { Link } from 'react-router';
import api from "api";

import Layout from "Layout";
import mui, { List, ListItem } from 'material-ui';

class ForumSideMenu extends React.Component {

  constructor(props) {
    super(props);

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
      <ul>
        {
          _.map(this.state.fora, (fora, cat_pk) =>
            <li key={cat_pk}>
              <p>{this.state.categories[cat_pk].titel}</p>
              <ul>
              {
                _.map(fora, (forum) => 
                   <li key={forum.pk}>
                     <Link to={`/forum/parts/${forum.pk}`}>{forum.titel}</Link>
                   </li>
                )
              }
              </ul>
            </li>
          )
        }
      </ul>
    );
  }
}

export default class Forum extends React.Component {
  render() {
    return (
      <Layout title="Reformaforum" sidemenu={ForumSideMenu}>
        {this.props.children}
      </Layout>
    );
  }
}
