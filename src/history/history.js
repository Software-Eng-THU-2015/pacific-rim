import React, {Component} from 'react';
import _ from 'lodash';

export default class History extends Component{
	constructor(props){
		super(props);
		this.state = {
			_days: []
		};
	}
	componentDidMount(){
		$.get("https://api.myjson.com/bins/3iknl", function(data){
			console.log(data);
			this.setState({
				_days: data.data
			});
		}.bind(this));
	}
	render(){
		let days = this.state._days;
		let cal = _.map(days, (item, idx) => { 
						if (item.status){
							return (<div key={idx} className="ui green circular label"> {item.day} </div>)
						}
						else{
							return (<div key={idx} className="ui red circular label"> {item.day} </div>)
						}
				});
		return(
				<div>
					History
					{cal}
				</div>
			  )
	}
}

