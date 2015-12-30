import React, { Component } from 'react';
// import AddPlan from './AddPlan';

import moment from 'moment';

export default class Tree extends Component{
    constructor(props){
		super(props);
	}
		
	getOpenid(){
		var _code;
		var reg = new RegExp("(^|&)code=([^&]*)(&|$)");
		var r = window.location.search.substr(1).match(reg);
		if(r!=null){
			_code = unescape(r[2]);
		} 
		else
			_code = "";
		$.getJSON("/apis/getOpenid", {code: _code}, function(data){
			
		});
	}
	
	componentDidMount(){
		var level = 0;
		var height = 0;
		var health = 0;
		var water = 0;
		var fertilizer = 0;
		var level_name = "";
    	var nowDate = new Date();
		
		this.getOpenid();
		
    	$.get("trees.json", function(data){
    		level = data.level;
    		height = data.height;
    		health = data.health;
    		water = data.water;
    		fertilizer = data.fertilizer;
			level_name: "";
			if(nowDate.getHours() < 6 || nowDate.getHours() > 18) {//for night
				$(".img").attr("src", level+"0.png")
			}else {//for day
				$(".img").attr("src", level+"1.png")
			}
    		$.getJSON("level.json", function(result){
    			$.each(result.result, function(i, field){
    	        	if(this.level == level){
    	        	    level_name = this.name;
    	        	}
    	    	});
				$(".level").text("lv"+level+": "+level_name+"");
    		});
			$(".health").text("健康度: "+health);
			$(".height").text("高度: "+height);
			$(".water").text("剩余浇水次数: "+water+"次");
			$(".fertilizer").text("剩余施肥次数: "+height+"次");
		});
	
		var self = this;
		$("#water").click(function(){
			if(water <= 0){
				alert("no more water to pour!");
			}else{
				var params = JSON.stringify({
					water: true,
					fertilizer: false
				});
				var id = self.props.params.id;
				var url = '/apis/tree/' + id + '/care_tree';
				$.post(url, params,
					function(){
					alert("pour water successfully!");
				});
			}
		});
		
		$("#fertilizer").click(function(){
			if(fertilizer <= 0){
				alert("no more fertilizer to feed!");
			}else{
				var params = JSON.stringify({
					water: false,
					fertilizer: true
				});
				var id = self.props.params.id;
				var url = '/apis/tree/' + id + '/care_tree';
				$.post(url, params,
				function(){
					alert("give fertilizer successfully!");
				});
			}
		});
    }
    render(){
	return(
		<div className="ui equal width center aligned padded grid">
	    	<div className="blue row">
		    	<h1>Tree</h1>
		    </div>
			<div className="row">
				<img className="ui img" style={{"width":"240px", "height":"400px"}}/>
			</div>
		<div className="row">
				<div className="ui list">
                    <h4><div className="item level">
                    </div></h4>
                    <div className="item health">
                    </div>
                    <div className="item height">
                    </div>
				</div>
			</div>
			<div className="grey row">
                <div className="column">
                    <div className="item water">
                    </div>
		 		    <input value = "浇水" type="submit" className="ui button" id="water" />
                </div>
			    <div className="column">
                    <div className="item fertilizer">
                    </div>
		 		    <input value = "施肥" type="submit" className="ui button" id="fertilizer" />
                </div>
            </div>
            <div className="black row">
            <h5>
                生命之树生长规则：完成每日打卡，奖励浇水机会一次<br/>
                完成每日挑战任务（每日一个），奖励施肥或浇水机会一次<br/>
                设健康度为x（0到10，初始为10）<br/>
                施肥：x大于等于6时，树高度增加2cm;x小于6的时候，树高度增加0.4*x cm;增加一点健康度（上限10）<br/>
                浇水：x大于等于6时，树高度增加1cm;x小于6的时候，树高度增加0.2*x cm;增加一点健康度（上限10）<br/>
                每日0点，所有树健康度降低1点，最低到0<br/>
                </h5>
            </div>
	    </div>
	)
    }


}
