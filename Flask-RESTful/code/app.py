from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'gabiroto'

jwt = JWT(app, authenticate, identity) # /auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self, name):
        # Next returns the first element, if called again the next one and so on
        # None is to return none in the case of no match
        item = next(filter(lambda x: x['name'] == name, items), None)
        # List returns a list of the filter object
        # item = list(filter(lambda x: x['name'] == name, item))
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': 'An item with name "{}" already exists.'.format(name)}, 400 #bad request

        data = Item.parser.parse_args()

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 #created

    def delete(self, name): 
        global items
        beforeDeleteLenght = len(items)
        items = list(filter(lambda x: x['name'] != name, items))
        if len(items) < beforeDeleteLenght:
            return {'message': 'Item deleted'}
        else:
            return {'message': 'An item with name `{}` could not be found.'.format(name)}, 404 #not found

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else: 
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5000)
app.run(port=5000, debug=True)

# curl -X POST -I -d '{"name": "produtinho"}' -H "Content-Type: application/json" http://localhost:5000/item/oies
# curl -X GET -I http://localhost:5000/item/oies
