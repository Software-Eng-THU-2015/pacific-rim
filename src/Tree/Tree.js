import React, { Component } from 'react';
// import AddPlan from './AddPlan';


import moment from 'moment';



export default class Tree extends Component{

    render(){

	$.get("/", function(data){
			level = data.level;
			health = data.health;
			height = data.hetight;
			water = data.water;
			fertilizer = data.fertilizer;
		});



	$(".img").attr("src", level+".png")
	$(".level").text("lv"+level+"��");
	$(".health").text("�����ȣ�"+health);
	$(".height").text("�߶ȣ�"+height);
	$(".water").text("ʣ�ཽˮ������"+water+"��");
	$(".fertilizer").text("ʣ��ʩ�ʴ�����"+height+"��");

	$("water").click(function(){
		if(water <= 0){
			alert("no more water to pour!");
		}else{
			$.post("/",{
				water: True,
				fertilizer: False
			},
			function(){
				alert("pour water successfully!");
			});
		}
	});
	$("fertilizer").click(function(){
		if(fertilizer <= 0){
			alert("no more fertilizer to feed!");
		}else{
			$.post("/",{
				water: False,
				fertilizer: True
			},
			function(){
				alert("give fertilizer successfully!");
			});
		}
	});



	return(
		<div className="ui equal width center aligned padded grid">
	    	<div className="blue row">
		    	<h1>Tree</h1>
		    </div>
			<div className="row">
				<div className="ui img">
				</div>
				<div className="ui list">
                    <div className="item level">
                    </div>
                    <div className="item health">
                    </div>
                    <div className="item height">
                    </div>
				</div>
			</div>
			<div className="grey row">
                <div className="ui list">
                    <div className="item water">
                    </div>
		 		    <input type="submit" className="ui item button" id="water"} />
                </div>
			    <div className="ui list">
                    <div className="item fertilizer">
                    </div>
		 		    <input type="submit" className="ui item button" id="fertilizer" />
                </div>
            </div>
            <div className="">
                ����֮����������xxxxx
            </div>
	    </div>
	)
    }


}