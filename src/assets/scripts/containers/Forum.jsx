import React, {PropTypes} from 'react';
import { connect } from 'react-redux';
import $ from 'jquery';
import _ from 'underscore';
import { Link } from 'react-router';
import Layout from '../components/Layout';
import * as actions from '../actions';

function loadData(props) {
  let { dispatch } = props;

  dispatch(actions.forum.loadList());
}

export class ForumSideMenu extends React.Component {

  static get propTypes() {
    return {
      forums: PropTypes.object.isRequired
    };
  }

  componentWillMount() {
    loadData(this.props);
  }

  render() {
    let { forums } = this.props;
    let grouped_forums = _(forums).groupBy((forum) => forum.categorie.pk);
    let categories = _(grouped_forums).map((forums) => forums[0].categorie);

    return (
      <ul>
        {
          _.map(grouped_forums, (forums, cat_pk) =>
            <li key={cat_pk}>
              <p>{categories[cat_pk].titel}</p>
              <ul>
              {
                _.map(forums, (forum) => 
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

export class Forum extends React.Component {

  static get propTypes() {
    return {
      forums: PropTypes.object.isRequired
    };
  }

  render() {
    return (
      <Layout title="Reformaforum" sidemenu={ForumSideMenu} sidemenuProps={this.props}>
        {this.props.children}
      </Layout>
    );
  }
}

function select(state, props) {
  let { entities : { forums }} = state;

  return {
    forums: forums
  };
}

export default connect(select)(Forum);
