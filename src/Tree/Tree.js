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

        if(nowDate.getHours() < 6 || nowDate.getHours() > 18) {//for night
			$("#img").attr("src", "/img/00.png")
		}else {//for day
			$("#img").attr("src", "/img/01.png")
		}
        $(".level").text("lv0: 树芽");
		$(".health").text("健康度: 0");
		$(".height").text("高度: 0");
		$(".water").text("剩余浇水次数: 0次");
		$(".fertilizer").text("剩余施肥次数: 0次");

    	$.get("trees.json", function(data){
    		level = data.level;
    		height = data.height;
    		health = data.health;
    		water = data.water;
    		fertilizer = data.fertilizer;
			if(nowDate.getHours() < 6 || nowDate.getHours() >1) {//for night
				$("#img").attr("src", "/img/"+level+"0.png")
			}else {//for day
				$("#img").attr("src", "/img/"+level+"1.png")
			}
            var obj = JSON.parse(level_list);
    		level_name = level_list[level].name;
            $(".level").text("lv"+level+": "+level_name+"");
			$(".health").text("健康度: "+health);
			$(".height").text("高度: "+height);
			$(".water").text("剩余浇水次数: "+water+"次");
			$(".fertilizer").text("剩余施肥次数: "+height+"次");
		});

		$("#water").click(function(){
			if(water <= 0){
				alert("no more water to pour!");
			}else{
				$.post("/care_tree",{
					water: True,
					fertilizer: False
				},
				function(){
					alert("pour water successfully!");
				});
			}
		});
		$("#fertilizer").click(function(){
			if(fertilizer <= 0){
				alert("no more fertilizer to feed!");
			}else{
				$.post("/care_tree",{
					water: False,
					fertilizer: True
				},
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
			<div className="ui segment">
                <img id="img" className="ui small left floated image" />
                <p className="item level">
                </p>
                <p className="item health">
                </p>
                <p className="item height">
                </p></div>
			<div className="grey row">
                <div className="column">
                    <div className="item water">
                    </div>
		 		    <input type="submit" className="ui button" id="water" value="浇水" />
                </div>
			    <div className="column">
                    <div className="item fertilizer">
                    </div>
		 		    <input type="submit" className="ui button" id="fertilizer" value="施肥" />
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
