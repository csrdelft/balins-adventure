import React from 'react';
import Layout from './Layout';

// simple 404 child view
export default class NotFound extends React.Component {
  render() {
    return <Layout title="404">
      <div>
        <h1>Niks hier, behalve een 404</h1>
      </div>
    </Layout>;
  }
}

