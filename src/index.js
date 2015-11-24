import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link } from 'react-router';
import App from './App';
import About from './About';

// ReactDOM.render(<App />, document.getElementById('root'));

ReactDOM.render((
    <Router>
	<Router path='/' component={App}>
	</Router>
	<Router path="about" component={About} />
    </Router>
), document.getElementById('root'));

