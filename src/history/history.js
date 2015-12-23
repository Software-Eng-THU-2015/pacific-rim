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
			else if (item.status){
				cell = (<div key={idx} className="column"><div className="ui green circular label"> {item.day} </div></div>)
			}
			else{
				cell = (<div key={idx} className="column"><div className="ui grey circular label"> {item.day} </div></div>)
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
				<div className = "grey row"><button onClick = {this.last} className="ui teal button"> Last </button></div>
				</div>
			</div>
		)
	}
}

