import React, {Component} from 'react';
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
		var url = '/apis/tags/' + user_id + '/get_tag_list';
		$.get(url, function(data){
			console.log(data);
			this.setState({
				tags: data.list
			});
		}.bind(this));
	}
	render(){
		var list = _.map(this.state.tags, (item)=>{
			return (
				<div key={item.id} className="item">
					<div className="content">
						<div className="header">
							{item.content}
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
