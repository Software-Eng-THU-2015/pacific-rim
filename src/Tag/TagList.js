import React, {Component} from 'react';
import moment from 'moment';
import _ from 'lodash';

export default class TagList extends Component{
	constructor(props){
		super(props);
		this.state = {
			tags: [],
		};
	}
	componentDidMount(){
		var user_id = this.props.params.id;
		var url = '/apis/tags/get_tag_list';
		$.get(url, {"user_id": user_id}, function(data){
			console.log(data);
			this.setState({
				tags: data.list
			});
		}.bind(this));
	}
	render(){
		var list = _.map(this.state.tags, (item)=>{
			var start_time = moment(item.start_time).format('MM-DD HH:mm');
			var end_time = moment(item.end_time).format('MM-DD HH:mm');
			return (
				<div key={item.id} className="item">
					<div className="ui card">
						<div className="content">
							<div className="header">
								{item.content}
							</div>
							<div className="meta">
								{start_time}
							</div>
							<div className="meta">
								{end_time}
							</div>
						</div>
					</div>
				</div>
				)
		});
		return(
				<div className="ui middle aligned animated list">
					{list}
				</div>
		)
	}
}
