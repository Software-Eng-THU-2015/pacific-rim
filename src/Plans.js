import React, { Component } from 'react';
// import AddPlan from './AddPlan';

// import TimePicker from 'react-clock-timepicker';

import TimePicker from 'react-timepicker';
require('./timepicker.css');
// import TimePicker from './TimePicker';

export default class Plans extends Component {
    onChange(hours, minutes){
        console.log(hours, minutes);
    }
    render(){
	return(
	    <div>
		<h1> Plans </h1>
		<TimePicker onChange={this.onChange} />
	    </div>
	)
    }
}
