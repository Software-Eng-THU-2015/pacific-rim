import React, {Component} from 'react';

export default class Daily extends Component{
	constructor(props){
		super(props);
		let today = new Date();
		let _mon = today.getMonth();
		let _year = today.getFullYear();
		this.state={
			month: _mon,
			year: _year,
			status: false
		};
	}
	componentDidMount(){
		$.get('/',{year: this.state.year, month: this.state.month}, (data)=>{
			console.log(data);
			if(data.status){
				this.setState({
					status: true
				});
			}
		});
	}
	handleBtnClick = (e) => {
		let btn = this.refs.submit;
		btn.classList.add('teal');
		$.post('', {month: this.state.month, year: this.state.year},
				(data)=>(console.log(data)));
	}
	render(){
		if (this.state.status){
			var btn = (
				<button ref="submit" onClick={this.handleBtnClick} className="ui teal button">Submit</button>
					)
		}
		else{
			var btn = (
				<button ref="submit" onClick={this.handleBtnClick} className="ui button">Submit</button>
					)
		}
		return (
				<div className="ui container">
					<div className="ui large header">
						{this.state.year}
					</div>
					<div className="ui header">
						{this.state.month}
					</div>
					{btn}
				</div>
			   )
	}
}
