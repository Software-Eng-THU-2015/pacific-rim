import React, {Component} from 'react';
import _ from 'lodash';
import urls from '../constants';
import moment from 'moment';
import classNames from 'classnames';
import Scroll from 'react-scroll';
import reactMixin from 'react-mixin';

export default class History extends Component{
	render(){
		var date = new Date();
		return (
			<Cal month={date.getMonth()} year={date.getFullYear()} />
			   )
	}
}
class Cal extends Component{
	constructor(props){
		super(props);
		const id = this.props.params.id;
		this.state = {
			_days: [],
			currentMon: this.props.month + 1,
			currentYear: this.props.year
		};
		console.log(this.state);
	}
	componentDidMount(){
		console.log(this.openid);
		function getOpenid(month, year, obj){
			var _code;
			var reg = new RegExp("(^|&)code=([^&]*)(&|$)");
			var r = window.location.search.substr(1).match(reg);
			if(r!=null){
				_code = unescape(r[2]);
			} 
			else
				_code = "";
			$.getJSON("/apis/getOpenid", {code: _code}, function(data){
				window.location.href = "http://59.66.139.53/user/"+ data.openid +"/history";
			});
		}
		
		if(window.location.href.substr(25, 4) == "shit"){
			getOpenid();
		}
		
		$.get("http://59.66.139.14/apis/getHistory",{month: this.state.currentMon, year: this.state.currentYear,
				openid: this.props.openid}, function(dt){
				console.log(dt);
				obj.setState({
					_days: dt.data
				});
		}.bind(this));
	
		
/*		$.get("dates.json", function(data){
			console.log(data);
			this.setState({
				_days: data.data
			});
		}.bind(this)); */
	}
	handleClickLast(){
		console.log('net');
	}

	
	prev = () =>{
	}
	render(){
		let days = this.state._days;
		for (var i = days.length; i < 35; i++){
			days.push({"day":0});
		}
		let cal = new Array(5);
		for (var i = 0; i < 5; i++){
			cal[i] = _.map(days.slice(i * 7, i * 7 + 7), (item, idx) => { 
			var cell, _cell;
			if (item.day == 0){
				cell = (<div key={idx} className="column"></div>)
			}
			else if (item.status == "false"){
				cell = (<div key={idx} className="column"><div className="ui grey square label"> {item.day} </div></div>)
			}
			else{
				cell = (<div key={idx} className="column"><div className="ui greeen square label"> {item.day} </div></div>)
			}
			return cell;
			});
		}
		return(
			<div>
				<div className="ui equal width center aligned padded grid">
				<div className = "blue row"><h1>history</h1></div>
					<div className = "row">
					<div className = "column"><h2>{this.state.currentMon}</h2></div>
					<div className = "column"><h2>{this.state.currentYear}</h2></div>
					</div>
					<div className = "row">{cal[0]}</div>
					<div className = "row">{cal[1]}</div>
					<div className = "row">{cal[2]}</div>
					<div className = "row">{cal[3]}</div>
					<div className = "row">{cal[4]}</div>
					<div className = "row"></div>
				<div className = "grey row"><div className="column"><button onClick = {this.last} className="ui teal button"> Last </button></div>
				<div className = "column"><button onClick = {this.next} className="ui teal button"> Next </button></div></div>
				</div>
			</div>
		)
	}
}

