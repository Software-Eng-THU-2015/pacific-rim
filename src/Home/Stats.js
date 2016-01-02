import React, { Component } from 'react';

export default class Stats extends Component {
  render() {
    return (
	<div> 
		<div className = "col-xs-12 label label-primary">
		    <h1> 900 Miles </h1>
		</div>
		<div className = "col-xs-6 label label-info">
		    <h2>10017 Steps</h2> 
		</div>
		<div className = "col-xs-6 label label-info">
		    <h2>600k Calorie</h2>
		</div>
	</div>
    );
  }
}
