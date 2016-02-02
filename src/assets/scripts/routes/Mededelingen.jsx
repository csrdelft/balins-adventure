import React from 'react';
import { IndexRoute, Route } from 'react-router';

import Mededelingen from '../containers/Mededelingen';
import MededelingDetail from '../components/MededelingDetail';

export default <Route component={Mededelingen}>
  <IndexRoute component={null} />
  <Route path=":pk" component={MededelingDetail} />
</Route>;
