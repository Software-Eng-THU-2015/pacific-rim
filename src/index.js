import React from 'react';
import ReactDOM from 'react-dom';
import { browserHistory, Router, Route, Link } from 'react-router';
import App from './App';
import Stats from './Home/Stats';
import Frame from './Home/Frame';
import About from './About';
import Tags from './Tag/Tags';
import Plan from './Plan/Plan';
import History from './history/history';
import Daily from './Daily/daily';
import TodoApp from './components/TodoApp.react';
import Tree from './Tree/Tree'

// import TimePicker from 'react-timepicker';

ReactDOM.render((
    <Router history={browserHistory}>
		<Router path='/' component={App}>
			<Router path='user/:id/stat' component={Stats} />
			<Router path='user/:id/chart' component={Frame} />
			<Router path='user/:id/tag' component={Tags} />
			<Router path='user/:id/plan' component={Plan} />
			<Router path='user/:id/daily' component={Daily} />
			<Router path='user/:id/todo' component={TodoApp} />
			<Router path='user/:id/tree' component={Tree} />
			<Router path='user/:id/history' component={History} />
		</Router>
    </Router>
), document.getElementById('root'));
