import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import items
from .schemas import ItemSchema, ItemUpdateSchema

ItemBlueprint = Blueprint('item', __name__, description='Operations on items')

@ItemBlueprint.route('/item/<string:item_id>')
class Item(MethodView):
    @ItemBlueprint.response(200, ItemSchema)
    def get(self, item_id):
        try:  
            return items[item_id], 201
        except KeyError:
            abort(404, message='Item not found')        
    
    @ItemBlueprint.arguments(ItemUpdateSchema)
    @ItemBlueprint.response(200, ItemSchema)
    def put(self, item_data, item_id):
        # item_data = request.get_json()    
        try:
            item = items[item_id]
            item.update(item_data)
            return item, 201

        except KeyError:
            abort(404, message='Item not found')

    def delete(self, item_id):            
        try:  
            del items[item_id]
            return {'messaje': "Item deleted"}
        except KeyError:
            abort(404, message='Item not found')   


@ItemBlueprint.route('/item')
class ItemList(MethodView):
    @ItemBlueprint.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    @ItemBlueprint.arguments(ItemSchema)
    @ItemBlueprint.response(201, ItemSchema)
    def post(self, item_data):        
        # item_data = request.get_json()
        for item in items.values():
            if(
                item_data['name']==item['name']
                and item_data['store_id'] == item['store_id']
            ):
                abort(400, message=f'Item already exists')
            

        item_id = uuid.uuid4().hex
        item = {**item_data, 'id': item_id}
        items[item_id] = item
        return item

