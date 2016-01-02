import React, { Component } from 'react';

import DatePicker from 'react-datepicker';
import moment from 'moment';


import 'react-datepicker/dist/react-datepicker.css';
import './tags.css';

export default class AddPlan extends Component{
    constructor(props){
		super(props);
		var myopenid;
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
		this.myopenid = id;
		console.log(id);
		$('.ui.accordion').accordion();
    }
    render(){
		return(
<div>
	<div className="col-xs-12 label label-primary">
		<h1>New Plan</h1>
	</div>
	<div className="col-xs-12 label label-primary">
		<div className="ui input">
			<input placeholder="计划每日里程数" type="text" ref="goal" />
		</div>
	</div>
	<div className="col-xs-12 label label-default">
		<div className="ui input">
			<input placeholder="起个好听的名字" type="text" ref="description" />
		</div>
	</div>
	<div className="col-xs-12 ui accordion">
		<div className="title">
			<h2>StartDate:</h2>
			<DatePicker selected={this.state.startDate}
			onChange={this.handleStartDate} />
		</div>

		<div className="title">
			<h2>EndDate :</h2>
			<DatePicker selected={this.state.endDate} onChange={this.handleEndDate} />
		</div>
	</div>
	<div className="col-xs-12 label label-default">
		<input ref="submit" type="submit" className="ui button"
		onClick={this.handleSubmit} />
	</div>
</div>
		)
    }

	handleSubmit = (e) =>{
		e.preventDefault();
		let goal = this.refs.goal.value;
		let description = this.refs.description.value;
		let startTime = this.state.startDate;
		startTime = startTime.set({
			hour: 0,
			minute: 0,
		});
		let endTime = this.state.endDate;
		endTime = endTime.set({
			hour: 23,
			minute: 59,
		});
		if(isNaN(goal)){
			alert("亲，您的计划里程数好像不太对哦~");
			return;
		}
		$.post('/apis/plans/create/',JSON.stringify({
				openid: this.myopenid,
				PL_TimeFrom:startTime,
				PL_TimeTo:endTime,
				PL_Goal:goal,
				PL_Description:description,
			}), function(data){
				if(data.res == 'ok'){
					this.refs.submit.classList.add('teal');
					this.props.onSubmit();
				}
				else{
					alert("您还有未结束的计划呢~");
				}
			}.bind(this));
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
