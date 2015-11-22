import React, { Component } from 'react';

import { Router, Route, Link } from 'react-router';

import Stats from './Stats';
import Frame from './Frame';

import About from './About';

export default class App extends Component {
  render() {
    return (
	<div>
	    <ul>
		<li><Link to='/about'>About</Link></li>
	    </ul>
	    {this.props.children}
	    <Stats />
	    <Frame />
	</div>
    );
  }
}
