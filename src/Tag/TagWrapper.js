import React, { Component } from 'react';

import Tags from './Tags';
import TagList from './TagList';

export default class TagWrapper extends Component{
	render(){
		return (
			<div className="ui two column middle aligned very relaxed stackable grid">
				<div className="column">
					<Tags {...this.props} />
				</div>
				<div className="ui vertical divider">
					OR
				</div>
				<div className="center aligned column">
					<TagList {...this.props} />
				</div>
			</div>
				)
	}
}
