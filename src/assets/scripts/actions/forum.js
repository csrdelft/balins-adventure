import api from '../utils/api';
import { normalize, Schema, arrayOf } from 'normalizr';
import createDetailActions from './createDetailActions';
import createListActions from './createListActions';

import * as meta from './meta';

export const REQUEST_FORUM_LIST = 'REQUEST_FORUM_LIST';
export const RECEIVE_FORUM_LIST = 'RECEIVE_FORUM_LIST';
export const REQUEST_DRAAD_LIST = 'REQUEST_DRAAD_LIST';
export const RECEIVE_DRAAD_LIST = 'REQUEST_DRAAD_LIST';

export const REQUEST_POST_DELETE = 'REQUEST_POST_DELETE';
export const RECEIVE_POST_DELETE = 'RECEIVE_POST_DELETE';

const Forum = new Schema('forums', {idAttribute: 'pk'});
const ShortForumDraad = new Schema('shortDraadjes', {idAttribute: 'pk'});
const ForumDraad = new Schema('draadjes', {idAttribute: 'pk'});
const ForumPost = new Schema('posts', {idAttribute: 'pk'});

ForumDraad.define({
  posts: {
    results: arrayOf(ForumPost)
  }
});

//
// Forum thread detail
//

export let forumDraad = Object.assign({}, 
  createDetailActions('ForumDraad', ForumDraad, api.forum.draadjes.get),
  createListActions('ForumDraad', {results : arrayOf(ShortForumDraad)}, (params => {
    let { pk , page } = params;
    return api.forum.draadjes.list(pk, page);
  })),
  {
    requestDeletePost: (pk) => {
      return {
        type: REQUEST_POST_DELETE,
        metatype: meta.REQUEST_DELETE_ENTITY,
        entityType: 'posts',
        pk
      };
    },

    receiveDeletePost: (pk) => {
      return {
        type: RECEIVE_POST_DELETE,
        metatype: meta.RECEIVE_DELETE_ENTITY,
        entityType: 'posts',
        pk
      };
    },

    deletePost: (pk) => {
      return dispatch => {
        dispatch(forumDraad.requestDeletePost(pk));

        api.forum.posts.delete(pk)
          .then((resp) => dispatch(forumDraad.receiveDeletePost(pk)))
          .catch((err) => console.error("Failed to delete post: " + err));
      };
    }
  }
);

//
// Forum (parts) list
// 

export let forum = createListActions('Forum', arrayOf(Forum), api.forum.list);
