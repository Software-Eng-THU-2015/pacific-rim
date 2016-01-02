import React, { Component } from 'react';

export default class Stats extends Component {
  render() {
    return (
	<div> 
		<div className = "col-xs-12 label label-primary" style={{"padding":"10px 10px 10px 10px"}}>
		    <h1> 900 Miles </h1>
		</div>
		<div className = "col-xs-6 label label-info" style={{"padding":"10px 10px 10px 10px"}}>
		    <h2>10017 Steps</h2> 
		</div>
		<div className = "col-xs-6 label label-info" style={{"padding":"10px 10px 10px 10px"}}>
		    <h2>600k Calorie</h2>
		</div>
	</div>
    );
  }
}
