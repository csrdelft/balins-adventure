import React from 'react';
import { IndexRoute, Route } from 'react-router';

import Mededelingen from './Mededelingen';
import MededelingDetail from './MededelingDetail';

export default <Route component={Mededelingen}>
  <IndexRoute component={null} />

  <Route path=":pk" component={MededelingDetail} />
</Route>;
