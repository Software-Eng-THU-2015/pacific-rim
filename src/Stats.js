import React, { Component } from 'react';

export default class Stats extends Component {
  render() {
    return (
	<div className = "ui equal width center aligned padded grid"> 
	    <div className = "row">
		<div className = "blue column">
		    <h1> 900 Miles </h1>
		</div>
	    </div>
	    <div className = "row"> 
		<div className = "column">
		    <h2>10017 Steps</h2> 
		</div>
		<div className = "column">
		    <h2>600k Calorie</h2>
		</div>
	    </div>
	</div>
    );
  }
}
