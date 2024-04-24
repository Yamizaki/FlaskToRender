from flask import Blueprint
from services.todo import createTodoService, getTodoService, getOneTodoService, updateTodoService, deleteTodoService
todo = Blueprint('todo', __name__)

@todo.route('/', methods=['GET'])
def getTodo():
    return getTodoService()

@todo.route('/<id>', methods=['GET'])
def get1Todo(id):
    return getOneTodoService(id)


@todo.route('/create', methods=['POST'])
def createTodo():
    return createTodoService()


@todo.route('/<id>', methods=['PUT'])
def updateTodo(id):
    return updateTodoService(id)

@todo.route('/<id>', methods=['DELETE'])
def deleteTodo(id):
    return deleteTodoService(id)