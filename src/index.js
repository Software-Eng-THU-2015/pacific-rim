import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link } from 'react-router';
import App from './App';
import About from './About';
import Tags from './Tag/Tags';

// import TimePicker from 'react-timepicker';

ReactDOM.render((
    <Router>
	<Router path='/' component={App}>
	    <Router path="about" component={About} />
	</Router>
	<Router path='tag' component={Tags} />
    </Router>
), document.getElementById('root'));

