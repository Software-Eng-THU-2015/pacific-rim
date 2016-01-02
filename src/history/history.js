
		import React, {Component} from 'react';
		import _ from 'lodash';

		export default class History extends Component{
			render(){
				var date = new Date();
				return (
					<Cal {...this.props} month={date.getMonth()} year={date.getFullYear()} />
					   )
			}
		}
		class Cal extends Component{
			constructor(props){
				super(props);
				this.state = {
					_days: [],
					currentMon: this.props.month + 1,
					currentYear: this.props.year
				};
				console.log(this.state);
			}
			componentDidMount(){
				var param = $.param({
					month: this.state.currentMon,
					year: this.state.currentYear,
					openid: this.props.params.id
				});
				
				
				function getOpenid(){
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
		
				$.get("/apis/getHistory", param, function(data){
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
					currentMon: month,
				});
				var param = $.param({
					month: month,
					year: year,
					openid: this.props.params.id
				});
				$.get("/apis/getHistory", param,  (data)=>{
					this.setState({
						_days: data.data
					})
				})
			}
			next = (e) => {
				var _month = this.state.currentMon + 1;
				var month = _month;
				var year = this.state.currentYear;
				if(_month==13){
					month = 1;
					year += 1;
				}
				console.log(month, year);
				this.setState({
					currentYear: year,
					currentMon: month
				});
				var param = $.param({
					month: month,
					year: year,
					openid: this.props.params.id
				});
				$.get("/apis/getHistory", param,  (data)=>{
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
				cell = (<td key={idx}></td>)
			}

			else if (item.status == "true"){
				cell = (<td key={idx}><div className="ui green square label"> {item.day} </div></td>)
			}
			else{
				cell = (<td key={idx}><div className="ui grey square label"> {item.day} </div></td>)
			}
			return cell;
			});
		}
		return(
			<div>
				<div>
					<div className = "col-xs-12 label label-primary"><h1>History</h1></div>
					<div className = "col-xs-6 label-info"><h2>{this.state.currentMon}</h2></div>
					<div className = "col-xs-6 label-info"><h2>{this.state.currentYear}</h2></div>
					<div className = "col-xs-12">
						<table className = "table table-condensed">
						<thead><tr><th></th><th></th><th></th><th></th><th></th><th></th><th></th>
						</tr></thead>
						<tbody>
						<tr>{cal[0]}</tr>
						<tr>{cal[1]}</tr>
						<tr>{cal[2]}</tr>
						<tr>{cal[3]}</tr>
						<tr>{cal[4]}</tr>
						</tbody>
						</table>
					</div>
					<div className = "col-xs-12"></div>
					<div className = "col-xs-12 label label-default"><div className="col-xs-6"><button onClick = {this.last} className="ui teal button"> Last </button></div>
					<div className = "col-xs-6"><button onClick = {this.next} className="ui teal button"> Next </button></div></div>
				</div>
			</div>
		)
	}
}

