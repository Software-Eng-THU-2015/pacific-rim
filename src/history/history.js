import React, {Component} from 'react';
import _ from 'lodash';

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
		this.state = {
			_days: [],
			currentMon: this.props.month,
			currentYear: this.props.year
		};
		console.log(this.state);
	}
	componentDidMount(){
		var param = $.param({
			month: this.state.currentMon,
			year: this.state.currentYear
		});
		$.get("https://api.myjson.com/bins/3iknl", param, function(data){
			console.log(data);
			this.setState({
				_days: data.data
			});
		}.bind(this));
	}
	handleClickLast(){
		console.log('net');
	}
	last = (e) => {
		var _month = this.state.currentMon - 1;
		var month = _month;
		var year = this.state.currentYear;
		if(_month==0){
			month = 12;
			year -= 1;
		}
		console.log(month, year);
		this.setState({
			currentYear: year,
			currentMon: month
		});
		var param = $.param({
			month,
			year
		});
		$.get("", param,  (data)=>{
			this.setState({
				_days: data.data
			})
		})
	}
	prev = () =>{
	}
	render(){
		let days = this.state._days;
		let cal = _.map(days, (item, idx) => { 
			var cell, _cell;
			if (item.status){
				cell =  (<div key={idx} className="ui green circular label"> {item.day} </div>)
			}
			else{
				cell =  (<div key={idx} className="ui red circular label"> {item.day} </div>)
			}
			return cell;
		});
		return(
			<div>
			history
				<div className="ui centered grid">
					{this.state.currentMon}
					{this.state.currentYear}
					{cal}
				</div>
				<button onClick = {this.last} className="ui teal button"> Last </button>
			</div>
		  )
	}
}

