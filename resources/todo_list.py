import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from .schemas import TodoListSchema


TodoListBlueprint = Blueprint('todo-lists', __name__, description='Operations on Todo lists')

@TodoListBlueprint.route('/todo-lists/<string:todo_list_id>')
class Store(MethodView):
    @TodoListBlueprint.response(200, TodoListSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message='Store not found')

    def delete(self, store_id):
        try:  
            del stores[store_id]
            return {'messaje': "Store deleted"}
        except KeyError:
            abort(404, message='Store not found')


@TodoListBlueprint.route('/todo-lists')
class StoreList(MethodView):
    @TodoListBlueprint.response(200, TodoListSchema(many=True))
    def get(self):
        return stores.values()

    @TodoListBlueprint.arguments(TodoListSchema)
    @TodoListBlueprint.response(201, TodoListSchema)
    def post(self, store_data):
        for store in stores.values()        :
            if store_data['name'] == store['name']:
                abort(400, message=f'Store already exists')
        store_id = uuid.uuid4().hex
        store =   { **store_data, 'id': store_id}
        stores[store_id] = store
        return store
