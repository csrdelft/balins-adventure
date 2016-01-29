import api from '../utils/api';
import { normalize, Schema, arrayOf } from 'normalizr';
import { combineReducers } from 'redux';

export * from './profiel';
export * from './forum';
export * from './auth';

// re-export router actions
import { routeActions } from 'react-router-redux';
export let router = routeActions;
