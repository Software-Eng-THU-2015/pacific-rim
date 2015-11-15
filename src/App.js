import React, { Component } from 'react';

import Stats from './Stats';
import Frame from './Frame';

export default class App extends Component {
  render() {
    return (
	<div>
	    <Stats />
	    <Frame />
	</div>
    );
  }
}
