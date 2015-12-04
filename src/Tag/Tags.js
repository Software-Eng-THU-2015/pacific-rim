import React, { Component } from 'react';
// import AddPlan from './AddPlan';

// import TimePicker from 'react-clock-timepicker';

import TimePicker from 'react-timepicker';
import DatePicker from 'react-datepicker';
import moment from 'moment';

import 'react-datepicker/dist/react-datepicker.css';
import './timepicker.css';

export default class Tags extends Component{
    constructor(props){
	super(props);
	this.state = {
	    startHour: 0,
	    startMin: 0,
	    endHour: 0,
	    endMin: 0,
	    startDate: moment(),
	    endDate: moment(),
	    tag: ''
	}
    }
    render(){
	return(
	    <form className="ui form">
		<div className="field">
		    <label>StartTime</label>
		    <DatePicker selected={this.state.startDate}
			onChange={this.handleStartDate} />
		</div>
		<div className="field">
		    <TimePicker onChange={this.handleStartTime} />
		</div>
		<div className="field">
		    <label>EndTime</label>
		    <DatePicker selected={this.state.endDate}
			onChange={this.handleEndDate} />
		</div>
		<div className="field">
		    <TimePicker onChange={this.handleEndTime} />
		</div>
		<div className="field">
		    <label>Tag</label>
		    <input type="text" ref="tag" />
		</div>
		<div className="field">
		    <input type="submit" className="ui button"
		    onClick={this.handleSubmit} />
		</div>
	    </form>
	)
    }
    handleSubmit = (e) =>{
	e.preventDefault();
	let tag = this.refs.tag.value;
	let startTime = this.state.startDate;
	startTime = startTime.set({
	    hour: this.state.startHour,
	    minute: this.state.startMin,
	});
	let endTime = this.state.endDate;
	endTime = endTime.set({
	    hour: this.state.endHour,
	    minute: this.state.endMin,
	});
	fetch('/tags/submit',{
	    method: 'post',
	    body: JSON.stringify({
		startTime,
		endTime,
		tag,
	    })
	})
    }
    handleEndDate = (date) =>{
	this.setState({
	    endDate: date
	})
    }
    handleStartDate = (date) =>{
	this.setState({
	    startDate: date
	})
    }
    handleStartTime = (hours, minutes) => {
	this.setState({
	    startHour: hours,
	    startMin: minutes
	})
    }
    handleEndTime = (hours, minutes) =>{
	this.setState({
	    endHour: hours,
	    endMin: minutes
	})
    }
}

