import React, { Component } from 'react';
import Chart from './Chart';
import TagList from './TagList'

export default class Frame extends Component {
  constructor(props){
      super(props);
      this.state = {source:'https://api.myjson.com/bins/1r1al'};
  }

  componentDidMount(){
      var dataUrls = [
	  'https://api.myjson.com/bins/1r1al',
	  'https://api.myjson.com/bins/4mcfh',
	  'https://api.myjson.com/bins/2ar65'
      ];
      var self = this;
      $('.ui.button').click(function(){
	  $(this).siblings().removeClass('active');
	  $(this).toggleClass('active');
	  var idx = $(this).index();
	  self.setState({source : dataUrls[idx]});
      });
  }


  render() {
    return (
	<div>
	    <div className = "ui three top attached buttons">
		<div className = "ui active button">Day</div>
		<div className = "ui button">Week</div>
		<div className = "ui button">Month</div>
	    </div>
	    <div className = "ui attached segment">
		<Chart source = {this.state.source} />
		<TagList startTime={"heihei"} endTime={"heihei"} />
	    </div>
	</div>
    );
  }
}
