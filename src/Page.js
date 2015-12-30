import React, { Component } from 'react';

import TagWrapper from './Tag/TagWrapper';
import SparkLines from './Home/SparkLines';

export default class Page extends Component{
	constructor(props){
		super(props);
		this.state = {
			displayTag: false,
		}
	}

	showTagWrapper = (e) => {
		e.preventDefault();
		var display = this.state.displayTag;
		this.setState({
			displayTag: !display,
		});
	}

	render(){
		var Tags;
		if(this.state.displayTag){
			Tags = <TagWrapper {...this.props} />;
		} else {
			Tags = <i className="tags icon" />
		}
		return(
			<div className="ui container">
				<SparkLines {...this.props} />
				<div className="ui centered grid">
					<div className="row">
						<div className="ui tag blue label" onClick={this.showTagWrapper}> Show Tags </div>
					</div>
					<div className="row">
						{Tags}
					</div>
				</div>
			</div>
			  )
	}
}
