import React, { Component } from 'react';

import { Router, Route, Link } from 'react-router';
import About from './About';
import Tags from './Tag/Tags';
import Stats from './Stats';
import History from './history/history';
import Daily from './Daily/daily';
import TodoApp from './components/TodoApp.react';
import Tree from './Tree/Tree';


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
		<li><Link to='/tree'>Tree</Link></li>
	    </ul>
	    {this.props.children}
			<Stats />
	</div>
    );
  }
}
