import React, { Component } from 'react';
import AddPlan from './AddPlan';
import urls from '../constants';
import _ from 'lodash';
import moment from 'moment';
import classNames from 'classnames';
import './tags.css';
import Scroll from 'react-scroll';
import reactMixin from 'react-mixin';

var Link = Scroll.Link;
var Element = Scroll.Element;
var Events = Scroll.Events;

export default class Plan extends Component{
	constructor(props){
		super(props);
		const id = this.props.params.id;
		this.state = {
			planlist: [],
		}
	}
	
	updateData = () =>{
		var params = {
			'openid': this.props.params.id,
			'start': moment().startOf('d').toISOString(),
			'end': moment().endOf('d').toISOString(),
		}
		var url = '/apis/plans/get_list/';

		$.get(url, params, (data)=>{
			this.setState({
				plans: data.data,
			});
		});
	}
	componentDidMount(){
		var myopenid;
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
				window.location.href = "http://59.66.139.53/user/"+ data.openid +"/plan";
			});
		}
		
		if(window.location.href.substr(25, 4) == "shit"){
			getOpenid();
		}
		
		this.updateData();
		
		this.scrollEvent.register('begin', () =>{
			console.log('begin', arguments);
		});
		this.scrollEvent.register('end', () =>{
			console.log('end', arguments);
		});
	}
	componentWillUnmount(){
		this.scrollEvent.remove('begin');
		this.scrollEvent.remove('end');
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
		this.updateData();
	}
	componentDidUpdate(){
	}
	render(){
		var plans = _.map(this.state.plans, (item, idx)=>{
			var BtnClass = classNames({
				'ui right floated button': true,
				'basic green': !item.status,
				'teal': item.status,
			})
			var start_time = moment(item.pl_time_from).format("YYYY-MM-DD HH:mm");
			var end_time = moment(item.pl_time_to).format( "YYYY-MM-DD HH:mm");
			console.log(start_time, end_time);
			return(
				<div key={idx} className="ui card">
					<div className="content">
						<div className="header">
							{item.pl_goal}
						</div>
						<div className="meta">
							{item.pl_description}
						</div>
						<div className="description">
							{start_time}
						</div>
						<div className="description">
							{end_time}
						</div>
					</div>
					<div className="extra content">
						<div ref="done" onClick={this.handleDone.bind(this, item)} className={BtnClass} >Done</div>
					</div>
				</div>
				)
		});
		return (
			<div className="ui centered grid">
				<div className="ui horizontal divider"> 
					<i className="check icon" />
					Plans of Today
				</div>
				<div className="ui segment">
					<div className="ui cards">
						{plans}
					</div>
				</div>
				<div className="ui horizontal divider"> 
					<i className="add icon" />
					Add A New Plan
				</div>
				<Element name="add_plan">
						<AddPlan onSubmit={this.updateData} {...this.props} id = {this.myopenid} />
				</Element>
				<div id="add">
					<Link to="add_plan" spy={true} smooth={true} duration={500} >
						<div className="ui red large tag label">
							<i className="ui add icon" />
						</div>
					</Link>
				</div>
			</div>
		)
	}
}

reactMixin(Plan.prototype, Events);
