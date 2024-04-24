from config.mongodb import mongo
from flask import request, Response


def createTodoService():
    data = request.get_json()
    
    title = data.get('title')
    description = data.get('description', None)
    
    if title:
        
        response = mongo.db.todos.insert_one({
                'title': title,
                'description': description,
                'done': False
            })
        result = {
            'id': str(response.inserted_id),
            'title': title,
            'description': description,
            'done': False
        }
        return  result
    else:
        return 'Invalid payload', 400
    
def getTodoService():
    from bson import json_util
    
    data = mongo.db.todos.find()
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')


def getOneTodoService(id):
    from bson import json_util, ObjectId
    
    data = mongo.db.todos.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

def updateTodoService(id):
    from bson import  ObjectId
    
    data = request.get_json()
    if len(data) == 0:
        return 'Invalid Update', 400
    
    result = mongo.db.todos.find_one({'_id': ObjectId(id)}, {'$set' : data})
    
    if result.modified_count > 1:
        return 'Succefully update', 200
    else:
        return 'Something went wrong', 404
   

def deleteTodoService(id):
    from bson import json_util, ObjectId
    
    data = mongo.db.todos.delete_one({'_id': ObjectId(id)})
  
    return 'Todo selected was delete'


 