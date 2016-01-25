import React from 'react';
import { Link, Route, IndexRoute } from 'react-router';

import ProfielDetail from '../containers/ProfielDetail';
import ProfielList from '../containers/ProfielList';
import VerticaleList from '../containers/VerticaleList';
import LedenLayout from '../components/LedenLayout';
//import VerticaleDetail from '../containers/VerticaleDetail';
//import CommissieList from "../containers/CommissieList";
//import KringList from "../containers/KringList";


/*
 <Route path="commissie" component={CommissieList}/>
 <Route path="kring" component={KringList}/>
 <Route path="verticale/:pk" component={VerticaleDetail}/>

</Route>*/

export default <Route>
  <IndexRoute component={ProfielList}/>
  <Route path=":pk" component={ProfielDetail}/>

  <Route path="groepen" component={LedenLayout}>
    <Route path="verticalen" component={VerticaleList}/>
  </Route>
</Route>;
