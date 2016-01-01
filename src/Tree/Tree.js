import React, { Component } from 'react';
// import AddPlan from './AddPlan';

import moment from 'moment';

export default class Tree extends Component{
    constructor(props){
		super(props);
	}
		
	
	componentDidMount(){
		/*var level_list = '{ "level_list2" : [' +
			'{"level":0, "name":"树芽"},' +
			'{"level":1, "name":"青树苗"},' +
			'{"level":2, "name":"小树"},' +
			'{"level":3, "name":"初生之树"},' +
			'{"level":4, "name":"弱冠之树"},' +
			'{"level":5, "name":"拔地之树"},' +
			'{"level":6, "name":"凌云之树"},' +
			'{"level":7, "name":"通天之树"},' +
			'{"level":8, "name":"银河之树"},' +
			'{"level":9, "name":"寰宇之树"} ]}';*/
        var level_list = [
			{"level":0, "name":"树芽"},
			{"level":1, "name":"青树苗"},
			{"level":2, "name":"小树"},
			{"level":3, "name":"初生之树"},
			{"level":4, "name":"弱冠之树"},
			{"level":5, "name":"拔地之树"},
			{"level":6, "name":"凌云之树"},
			{"level":7, "name":"通天之树"},
			{"level":8, "name":"银河之树"},
			{"level":9, "name":"寰宇之树"}
        ];

		var level = 0;
		var height = 0;
		var health = 0;
		var water = 0;
		var fertilizer = 0;
		var level_name = "树芽";
    	var nowDate = new Date();
		var myopenid;
		
		function getTree(){
	    	$.getJSON("/apis/get_tree", {openid: myopenid}, function(data){
	    		level = data.level;
	    		height = data.height;
	    		health = data.health;
	    		water = data.water;
	    		fertilizer = data.fertilizer;
				if(nowDate.getHours() < 6 && nowDate.getHours() >1) {//for night
					$("#img").attr("src", "/img/"+level+"0.png")
				}else {//for day
					$("#img").attr("src", "/img/"+level+"1.png")
				}
				console.log(0);
				if(level == 0)
					level_name = "树芽";
				else if(level == 1)
					level_name = "青树苗";
				else if(level == 2)
					level_name = "小树";
				else if(level == 3)
					level_name = "初生之树";
				else if(level == 4)
					level_name = "弱冠之树";
				else if(level == 5)
					level_name = "拔地之树";
				else if(level == 6)
					level_name = "凌云之树";
				else if(level == 7)
					level_name = "通天之树";
				else if(level == 8)
					level_name = "银河之树";
				else if(level == 9)
					level_name = "寰宇之树";
				
				
				/*
	            var obj = JSON.parse(level_list);
	    		level_name = level_list[level].name;
				*/
				console.log(1);
	            $("#level").html("lv"+level+" : "+level_name+"");
				$("#health").html("健康度: "+ health);
				$("#height").html("高度: "+ height);
				$("#show_water").html("剩余浇水次数: "+ water+"次");
				$("#show_fertilizer").text("剩余施肥次数: " + fertilizer + "次");
				console.log(2);
			});
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
				myopenid = data.openid;
		    	getTree();
			});
		}
		
		
		
		getOpenid();
		
    	
	
		var self = this;
		$("#water").click(function(){
			if(water <= 0){
				alert("no more water to pour!");
			}else{
				var id = self.props.params.id;
				var url = '/apis/care_tree';
				$.post(url, {openid: myopenid,
					water: true,
					fertilizer: false},
					function(){
					alert("pour water successfully!");
					getTree();
				});
			}
		});
		
		$("#fertilizer").click(function(){
			if(fertilizer <= 0){
				alert("no more fertilizer to feed!");
			}else{
				var id = self.props.params.id;
				var url = '/apis/care_tree';
				$.post(url, {openid: myopenid,
					water: false,
					fertilizer: true},
					function(){
					alert("give fertilizer successfully!");
					getTree();
				});
			}
		});
    }
    render(){
	return(
		<div>
	    	<div className="col-xs-12 label label-primary">
		    	<h1>Tree</h1>
		    </div>
			<div className="col-xs-12">
		<img id="img" className="ui small left floated image" style = {{position:"relative", width: "62%", top: "8px"}}/>
				<div style = {{position:"relative", top: "50px", fontSize:"120%"}}>
                	<p className="item level" id = "level">
                	</p>
                	<p className="item health" id = "health">
                	</p>
                	<p className="item height" id = "height">
                	</p>
				</div>
		</div>
		
			<div className="col-xs-12 label label-default">
                <div className="col-xs-6">
                    <div className="item water" id = "show_water" style = {{position:"relative", bottom: "8px"}}>
						
                    </div>
		 		    <input type="submit" className="ui button" id="water" value="浇水" />
                </div>
			    <div className="cocol-xs-6">
                    <div className="item fertilizer" id = "show_fertilizer" style = {{position:"relative", bottom: "8px"}}>
						
                    </div>
		 		    <input type="submit" className="ui button" id="fertilizer" value="施肥" />

                </div>
            </div>
            <div className="col-xs-12 label label-success">
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
