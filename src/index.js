import React from 'react';
import ReactDOM from 'react-dom';
import { browserHistory, Router, Route, Link } from 'react-router';
import createBrowserHistory from 'history/lib/createBrowserHistory';

import App from './App';
import Stats from './Home/Stats';
import About from './About';
import TagWrapper from './Tag/TagWrapper';
import Plan from './Plan/Plan';
import History from './history/history';
import Daily from './Daily/daily';
import TodoApp from './components/TodoApp.react';
import Tree from './Tree/Tree'

import SparkLines from './Home/SparkLines';

const history = createBrowserHistory();

ReactDOM.render((
    <Router history={history}>
		<Router path='/' component={App}>
			<Router path='about' component={About} />

			<Router path='user/:id/chart' component={SparkLines} />

			<Router path='user/:id/stat' component={Stats} />
			<Router path='user/:id/tag' component={TagWrapper} />
			<Router path='user/:id/plan' component={Plan} />
			<Router path='user/:id/daily' component={Daily} />
			<Router path='user/:id/todo' component={TodoApp} />
			<Router path='user/:id/tree' component={Tree} />
			<Router path='user/:id/history' component={History} />
		</Router>
    </Router>
), document.getElementById('root'));
