import React, { Component } from 'react';
// import AddPlan from './AddPlan';

// import TimePicker from 'react-clock-timepicker';

import TimePicker from 'react-timepicker';
import DatePicker from 'react-datepicker';
import moment from 'moment';
import Cookie from 'js-cookie';

import TagList from './TagList';

import 'react-datepicker/dist/react-datepicker.css';
import './jquery-clockpicker.min.js';
import './jquery-clockpicker.min.css';
import './tags.css';
import './timepicker.js';

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
		$('.clockpicker').clockpicker();
    }
    render(){
	return(
		<div>
	    	<div className="col-xs-12 label label-primary" style={{"padding":"10px 10px 10px 10px"}}>
		    	<h1>Tag</h1>
		    </div>
		    <div className="col-xs-12 label label-primary" style={{"padding":"10px 10px 10px 10px"}}>
		    	<div className="ui input">
		    		<input type="text" ref="tag" />
	    		</div>
			</div>
			<div className="col-xs-12 ui accordion" style={{"padding":"10px 10px 10px 10px"}}>
				<div className="title">
		    		<h3><i className="dropdown icon"></i>StartTime:</h3>
			   		<DatePicker selected={this.state.startDate}
					onChange={this.handleStartDate} />
				</div>
				<div className={"content"}>
					<div className ="input-group clockpicker" style = {{"width": "64%", "left": "18%"}} data-placement="top" >
    					<input type="text" id = "startTime" className="form-control" value = "09:32"  onChange={this.handleStartTime}/>
    					<span className="input-group-addon">
        					<span className="glyphicon glyphicon-time">
							</span>
   						</span>
					</div>
				</div>
			
				<div className="title">
		    		<h3><i className="dropdown icon"></i>EndTime:</h3>
		    		<DatePicker selected={this.state.endDate}
					onChange={this.handleEndDate} />
				</div>
				<div className="content">
					<div className ="input-group clockpicker" style = {{"width": "64%", "left": "18%"}} data-placement="top" >
    					<input type="text" id = "endTime" className="form-control" value = "09:32" onChange={this.handleEndTime}/>
    					<span className="input-group-addon">
        					<span className="glyphicon glyphicon-time">
							</span>
   						</span>
					</div>
				</div>
			</div>
			<div className="col-xs-12 label label-default" style={{"padding":"10px 10px 10px 10px"}}>
		 		<input value = "创建标签" ref="submit" type="submit" className="ui button" onClick={this.handleSubmit} />
			</div>
		<script>
				$('.clockpicker').clockpicker();
		</script>
	    </div>				
	)
    }

    handleSubmit = (e) =>{
		e.preventDefault();
		let tag = this.refs.tag.value;
		let startTime = this.state.startDate;
		startTime = startTime.set({
			hour: parseInt($("#startTime").val()[0] + $("#startTime").val()[1]),
			minute: parseInt($("#startTime").val()[3] + $("#startTime").val()[4]),
		});
		let endTime = this.state.endDate;
		endTime = endTime.set({
			hour: parseInt($("#endTime").val()[0] + $("#endTime").val()[1]),
			minute: parseInt($("#endTime").val()[3] + $("#endTime").val()[4]),
		});
		$.post('/apis/tags/post_tag/', JSON.stringify({
				openid: this.props.params.id,
				TG_TimeFrom:startTime,
				TG_TimeTo:endTime,
				TG_Content:tag,
			}), function(data){
				if(data.res == 'ok'){
					this.refs.submit.classList.add('teal');
					window.location.href = window.location.href;
				}
				else{
					alert("");
				}
			}.bind(this));
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
    handleStartTime = (value) => {
		this.setState({
			startHour: parseInt(value[0] + value[1]),
			startMin: parseInt(value[3] + value[4])
		})
		console.log(startHour);
		alert(startHour);
		console.log(startMin);
    }
    handleEndTime = (value) =>{
		this.setState({
			endHour: parseInt(value[0] + value[1]),
			endMin: parseInt(value[3] + value[4])
		})
    }
}
