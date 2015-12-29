import React, { Component } from 'react';

import { Router, Route, Link } from 'react-router';
import About from './About';
import Tags from './Tag/Tags';
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

		<li><Link to='/user/shit/tag'>ShitTag</Link></li>
		<li><Link to='/user/shit/page'>Shit</Link></li>
		<li><Link to='/user/shit/chart'>ShitChart</Link></li>
		<li><Link to='/user/shit/stat'>ShitStat</Link></li>

		<li><Link to='/user/shit/plan'>ShitPlan</Link></li>

		<li><Link to='/user/shit/history'>History</Link></li>
		<li><Link to='/user/shit/daily'>Daily</Link></li>
		<li><Link to='/todo'>Todo</Link></li>
		<li><Link to='/user/shit/tree'>Tree</Link></li>
	    </ul>
	    {this.props.children}
	</div>
    );
  }
}
