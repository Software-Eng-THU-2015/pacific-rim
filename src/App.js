import React, { Component } from 'react';

import { Router, Route, Link } from 'react-router';

import Stats from './Stats';
import Frame from './Frame';

import About from './About';
import Tags from './Tag/Tags';
import History from './history/history';
import Daily from './Daily/daily';
// import ToDo from './components/todo';

export default class App extends Component {
  render() {
    return (
	<div>
	    <ul>
		<li><Link to='/about'>About</Link></li>
		<li><Link to='/tag'>Tags</Link></li>
		<li><Link to='/history'>History</Link></li>
		<li><Link to='/daily'>Daily</Link></li>
		<li><Link to='/todo'>Todo</Link></li>
	    </ul>
	    {this.props.children}
	    // <Stats />
	    // <Frame />
	</div>
    );
  }
}
