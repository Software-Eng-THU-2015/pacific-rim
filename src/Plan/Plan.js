import React, { Component } from 'react';
import AddPlan from './AddPlan';
import urls from '../constants';
import _ from 'lodash';
import classNames from 'classnames';

export default class Plan extends Component{
	constructor(props){
		super(props);
		this.state = {
			planlist: [],
		}
	}
	updateData = () =>{
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
	componentDidMount(){
		this.updateData();
	}
	handleDone = (item)=>{
		var pid = item.pl_id;
		console.log(pid);
		var url = '/apis/plans/' + pid + '/update/';
		fetch(url, {
			method: 'post',
			body: JSON.stringify({
				status: true,
			})
		}).then(res => {
			console.log(res.json())
		})
		this.refs.done.classList.add('teal');
	}
	componentDidUpdate(){
	}
	render(){
		var plans = _.map(this.state.plans, (item, idx)=>{
			var BtnClass = classNames({
				'ui button': true,
				'teal': item.status,
			})
			return(
				<div key={idx}>
					<div className="ui header">
						{item.pl_goal}
					</div>
					<div className="ui description">
						{item.pl_time_from}
					</div>
					<div className="ui description">
						{item.pl_time_to}
					</div>
					<div ref="done" onClick={this.handleDone.bind(this, item)} className={BtnClass} >Done</div>
				</div>
				)
		});
		return (
			<div>
				Plan of Today
				{plans}
				<AddPlan onSubmit={this.updateData} {...this.props} />
			</div>
		)
	}
}