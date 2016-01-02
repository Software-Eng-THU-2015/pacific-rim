import React, { Component } from 'react';

import TagWrapper from './Tag/TagWrapper';
import SparkLines from './Home/SparkLines';

export default class Page extends Component{
	constructor(props){
		super(props);
		this.state = {
			displayTag: false,
		}
		
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
				window.location.href = "http://162.243.136.148/user/"+ data.openid +"/page";
			});
		}
		
		if(window.location.href.substr(25, 4) == "shit"){
			getOpenid();
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
				<div className="col-xs-12">
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
