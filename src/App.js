import React, { Component } from 'react';

import { Router, Route, Link } from 'react-router';

import Stats from './Stats';
import Frame from './Frame';

import About from './About';
import Tags from './Tag/Tags';

export default class App extends Component {
  render() {
    return (
	<div>
	    <ul>
		<li><Link to='/about'>About</Link></li>
		<li><Link to='/tag'>Tags</Link></li>
	    </ul>
	    {this.props.children}
	    <Stats />
	    <Frame />
	</div>
    );
  }
}
