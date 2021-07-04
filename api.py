import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True
## Class to understand the order and the bill .
class Order : 
    def __init__(self,o) :
        cost = 0
        self.order = o
        print(o)
        for order in o["order_items"] : 
            cost += order["quantity"]*order["price"]
        offer_type = o["offer"]["offer_type"]
        delivery_fee = 0
        if o["distance"] < 10000 : 
                delivery_fee = 5000 
        elif o["distance"] <20000 : 
            delivery_fee = 10000
        elif o["distance"] < 50000 : 
            delivery_fee = 50000
        else : 
            delivery_fee = 100000
        if offer_type == "FLAT" : 
            discount = o["offer"]["offer_val"]
        else :      
            discount = delivery_fee
        cost += delivery_fee
        if cost > discount :
            cost = cost - discount
        else : 
            cost = 0

        dicti = {"order_total":cost}
        json_object = json.dumps(dicti)
        self.cost = json_object
        
## route to get the basic page
@app.route('/',methods = ['GET'])
def home() : 
    return '<h1> hi this is rushabh <h1>'
## route to get the order total , pass the order as the json format using python request
@app.route('/api/order_total/',methods = ['GET'])
def order_total() : 
    r = request.json    
    order = Order(r)
    
    return order.cost
        

#run the main function to get the app started at http://127.0.0..1:5000/
if __name__ == '__main__':
    app.run(debug=False)