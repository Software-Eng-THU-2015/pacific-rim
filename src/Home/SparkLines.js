import React, { Component } from 'react';
import ControllerChart from './Line';
import classNames from 'classnames';

var $ = jQuery = require('jquery');
import './Frame.css';

export default class SparkLines extends Component {
	constructor(props){
	    super(props);
		console.log(this.props.params.id);
		this.state = {
			currentID: 0,
		};
	}
	
	handleBtnClick(item){
		this.setState({
			currentID: item.id,
		}, function(){
			this.refs.chart.updateChart(item.id);
		});
	}

	componentDidMount(){
		this.setState({
			currentID: 0,
		});
	}


	render() {
		var btns = [
			{ label: 'week', id: 0,},
			{ label: 'doubleWeek', id: 1,},
			{ label: 'month', id: 2,}
		];
		var Buttons = _.map(btns, (item) => {
			var BtnClass = classNames({
				'ui button': true,
				'teal': item.id == this.state.currentID,
			});
			return (
				<div className = {BtnClass}  onClick={this.handleBtnClick.bind(this, item)} key = {item.id}>{item.label}</div>
				)
		});
		return (
		  <div>
			  <div className = "ui three top attached buttons">
				{Buttons}
			  </div>
			  <div className = "ui attached segment">
			  	<ControllerChart ref = "chart" id = {this.state.currentID} {...this.props} />
			  </div>
		  </div>
      );
  }
}
