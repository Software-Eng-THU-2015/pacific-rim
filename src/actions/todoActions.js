import AppDispatcher from '../dispatcher/AppDispatcher';
import appConstants from '../constants/appConstants';

export var todoActions =  {
	create: (text)=>{
				AppDispatcher.dispatch({
					actionType: appConstants.TODO_CREATE,
					text: text
				});
			},
	updateText: (id, text)=>{
					AppDispatcher.dispatch({
						actionType: appConstants.TODO_UPDATE_TEXT,
						id:id,
						text: text
					});
				},
	toggleComplete: (todo)=>{
						var id = todo.id;
						var actionType = todo.complete ?
							appConstants.TODO_UNDO_COMPLETE :
							appConstants.TODO_COMPLETE;
						AppDispatcher.dispatch({
							actionType,
							id
						});
					},
	toggleCompleteAll: ()=>{
						   AppDispatcher.dispatch({
							   actionType: appConstants.
							   TODO_TOGGLE_COMPELTE_ALL
						   })
					   },
	destroy: (id)=>{
				 AppDispatcher.dispatch({
					 actionType: appConstants.TODO_DESTROY,
				 	 id
				 })
			 },
	destroyCompleted: ()=>{
						  AppDispatcher.dispatch({
							  actionType: appConstants.
							  TODO_DESTROY_COMPLETED
						  });
					  }
}
