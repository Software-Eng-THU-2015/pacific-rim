import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link } from 'react-router';
import App from './App';
import About from './About';
import Tags from './Tag/Tags';
import Stats from './Stats';
import History from './history/history';
import Daily from './Daily/daily';
import TodoApp from './components/TodoApp.react';
import Tree from './Tree/Tree'

// import TimePicker from 'react-timepicker';

ReactDOM.render((
    <Router>
	<Router path='/' component={App}>
	    <Router path="about" component={About} />
	</Router>
	<Router path='tag' component={Tags} />
	<Router path='history' component={History} />
	<Router path='daily' component={Daily} />
	<Router path='todo' component={TodoApp} />
	<Router path='tree' component={Tree} />
    </Router>
), document.getElementById('root'));
