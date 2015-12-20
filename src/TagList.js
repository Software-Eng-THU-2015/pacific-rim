import React, {Component} from 'react';
import _ from 'lodash';

export default class TagList extends Component{
	constructor(props){
		super(props);
		this.state = {
			_tags: [{"tg_time_from":"jiba", "tg_time_to":"nojiba", "tg_content":"heiheihei"}],
			startTime: this.props.startTime,
			endTime: this.props.endTime
		};
		console.log(this.state);
	}
	componentDidMount(){
		var param = $.param({
			startTime: this.state.startTime,
			endTime: this.state.endTime
		});
		$.get("https://127.0.0.1/get_tag", param, function(data){
			console.log(data);
			this.setState({
				tags: data.entries
			});
		}.bind(this));
	}
	render(){
		let tags = this.state._tags;
		let tagLi = _.map(tags, (item, idx) => {
			var cell;
			cell = (
				<div key={idx} className="row">
					<div className="grey column"> {item.tg_time_from} </div>
					<div className="column"> {item.tg_time_to} </div>
					<div className="column"> {item.tg_content} </div>
				</div>
				)
			return cell;
		});
		return(
			<div>
				<div className="ui equal width center aligned padded grid">
				<div className="blue column"><h2>momoda</h2></div>
					{tagLi}
				</div>
			</div>
		)
	}
}
