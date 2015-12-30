import React, { Component } from 'react';
// import AddPlan from './AddPlan';

// import TimePicker from 'react-clock-timepicker';

import TimePicker from 'react-timepicker';
import DatePicker from 'react-datepicker';
import moment from 'moment';
import Cookie from 'js-cookie';

import TagList from './TagList';

import 'react-datepicker/dist/react-datepicker.css';
import './timepicker.css';
import './tags.css';

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
	componentDidMount(){
		const id = this.props.params.id;
		console.log(id);
		$('.ui.accordion').accordion();
    }
    render(){
	return(
		<div className="ui equal width center aligned padded grid">
	    	<div className="blue row">
		    	<h1>Tag</h1>
		    </div>
		    <div className="blue row">
		    	<div className="ui input">
		    		<input type="text" ref="tag" />
	    		</div>
			</div>
			<div className="ui accordion">
				<div className="title" style={{"width":"300px"}}>
		    		<h2><i className="dropdown icon"></i>StartTime :</h2>
			   		<DatePicker selected={this.state.startDate}
					onChange={this.handleStartDate} />
				</div>
				<div className="content">
		    		<TimePicker onChange={this.handleStartTime} />
				</div>
				<div className="title">
		    		<h2><i className="dropdown icon"></i>EndTime :</h2>
		    		<DatePicker selected={this.state.endDate}
					onChange={this.handleEndDate} />
				</div>
				<div className="content">
		    		<TimePicker onChange={this.handleEndTime} />
				</div>
			</div>
			<div className="grey row">
		 		<input ref="submit" type="submit" className="ui button"
		   		onClick={this.handleSubmit} />
			</div>
	    </div>
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

		fetch('/apis/tags/post_tag/',{
			method: 'post',
			body: JSON.stringify({
				openid: this.props.params.id,
				TG_TimeFrom:startTime,
				TG_TimeTo:endTime,
				TG_Content:tag,
			})
		}).then(res => {
			if(res.ok){
				this.refs.submit.classList.add('teal');
			}
		})
    }
	handleTagAdded = () => {
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
