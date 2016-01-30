import api from '../utils/api';
import { normalize, Schema, arrayOf } from 'normalizr';
import * as meta from './meta';
import {ShortProfiel} from './profiel';


export let auth = {

  REQUEST_LOGIN: "REQUEST_LOGIN",
  PRELOAD_LOGIN_SUCCESS: "PRELOAD_LOGIN_SUCCESS",
  LOGIN_SUCCESS: "LOGIN_SUCCESS",
  LOGIN_FAIL: "LOGIN_FAIL",

  login: function (user, pw) {
    return dispatch => {
      dispatch(auth.requestLogin(user, pw));
      return api.auth.login(user, pw)
        .catch(resp => dispatch(auth.loginFail(resp)))
        .then(resp => dispatch(auth.loginSuccess(resp)));
    };
  },

  requestLogin: function(user, pw) {
    return {
      type: auth.REQUEST_LOGIN,
      user
    };
  },

  preloadLogin: function(user) {
    return {
      type: auth.PRELOAD_LOGIN_SUCCESS,
      user
    };
  },

  loginSuccess: function(resp) {
    return {
      type: auth.LOGIN_SUCCESS,
      metatype: meta.RECEIVE_ENTITIES,
      response: normalize(resp, {data: ShortProfiel})
    };
  },

  loginFail: function(resp) {
    return {
      type: auth.LOGIN_FAIL,
      response: resp
    };
  }
};
