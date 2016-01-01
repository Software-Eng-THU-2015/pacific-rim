import React, { Component } from 'react';

import Tags from './Tags';
import TagList from './TagList';

export default class TagWrapper extends Component{
	render(){
		return (
			<div style={{"textAlign":"center"}}>
				<div className="col-xs-12">
					<TagList {...this.props} />
				</div>
				<div className="col-xs-12">
					<Tags {...this.props} />
				</div>
			</div>
				)
	}
}
