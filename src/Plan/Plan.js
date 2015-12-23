import React, { Component } from 'react';
import AddPlan from './AddPlan';
import urls from '../constants';
import _ from 'lodash';

export default class Plan extends Component{
	constructor(props){
		super(props);
		this.state = {
			planlist: [],
		}
	}
	componentDidMount(){
		var params = {
			'openid': this.props.params.id,
		}
		var url = '/apis/plans/get_today';

		$.get(url, params, (data)=>{
			this.setState({
				plans: data.data,
			});
		});
			
	}
	componentDidUpdate(){
	}
	render(){
		var plans = _.map(this.state.plans, (item, idx)=>{
			if(item.status){
				var mark = ( <div> Done </div>);
			}
			else{
				var mark = ( <div> Todo </div>);
			}
			return(
				<div>
					<div className="ui header">
						{item.pl_goal}
					</div>
					<div className="ui description">
						{item.pl_time_from}
					</div>
					<div className="ui description">
						{item.pl_time_to}
					</div>
						{mark}
				</div>
				)
		});
		return (
			<div>
				Plan of Today
				{plans}
				<AddPlan {...this.props} />
			</div>
		)
	}
}
