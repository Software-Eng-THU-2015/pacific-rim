import React, { Component } from 'react';
import moment from 'moment';
import _ from 'lodash';
import d3 from 'd3';
var $ = jQuery = require('jquery');


class Chart extends Component{
	render(){
		return(
				<svg width={this.props.width} height={this.props.height}>
					{this.props.children}
				</svg>
			  )
	}
}
class Line extends Component{
	render(){
			return (
				<path d={this.props.path} stroke={this.props.color}
				strokeWidth={this.props.width} fill='none' />
				)
	}
}
Line.defaultProps = {
	path: '',
	color: 'blue',
	width: 2
}

class DataSeries extends Component{
	render(){
		var self = this,
			props = this.props,
			xScale = props.xScale,
			yScale = props.yScale;
		var path = d3.svg.line()
			.x((d) => (xScale(d.x)))
			.y((d) => (yScale(d.y)))
			.interpolate(this.props.interpolate);
		return(
				<Line path={path(this.props.data)} 
				color={this.props.color} />
			  )
	}
}
DataSeries.defaultProps = {
	data: [],
	interpolate: 'linear'
}

class LineChart extends Component{
	render(){
		var data = this.props.data,
			size = { width: this.props.width, height: this.props.height};
		var max = _.chain(data.series1, data.series2)
			.zip()
			.map((vals) => (_.reduce(vals, (memo, value) => (Math.max(memo, value.y)), 0)))
			.max()
			.value();

		var xScale = d3.scale.linear()
			.domain([0, 6])
			.range([0, this.props.width]);

		var yScale = d3.scale.linear()
			.domain([0, max])
			.range([this.props.height, 0]);

		return (
			<Chart width={this.props.width} height={this.props.height}>
				<DataSeries data={data.series1} size={size} xScale={xScale} yScale={yScale} ref="series1" color="blue" />
				<DataSeries data={data.series2} size={size} xScale={xScale} yScale={yScale} ref="series2" color="red" />
			</Chart>
			)
	}
}
LineChart.defaultProps ={
	width: 600,
	height: 300
}

export default class ControllerChart extends Component{
	constructor(props){
		super(props);
		this.state = {
			data: [],
		};
	    var Url = '/apis/user/' + this.props.params.id + '/steps/';
	    var start_time = moment().subtract(7, 'd').toISOString(),
	    	end_time = moment().toISOString();
	    var weekUrl = Url + '?'  + $.param({
	    	start_time,
	    	end_time,
	    });
	    var doubleWeekUrl = Url + '?'  + $.param({
	    	'start_time': moment().subtract(14, 'd').toISOString(),
	    	'end_time': moment().toISOString(),
	    });
	    var monthUrl = Url + '?' + $.param({
	       'start_time': moment().subtract(30, 'd').toISOString(),
	       'end_time': moment().toISOString(),
	    });
	    this.dataUrls = [weekUrl, doubleWeekUrl, monthUrl];
	}
	componentDidMount(){
		this.updateChart(this.props.id);
	}
	updateChart(i){
		$.get(this.dataUrls[i], (res)=>{
			var arr1 = _.map(res.data, (item, idx) => ({x:idx, y:item.st_step_number})),
				arr2 = _.map(res.data, (item, idx) => ({x:idx, y:item.st_calorie}));
			var data = {};
			data.series1 = arr1;
			data.series2 = arr2;
			this.setState({
				data: data,
			});
			console.log(this.state.data);
		});
	}
	render(){
		return(
				<LineChart data={this.state.data} />
			)
	}
}
