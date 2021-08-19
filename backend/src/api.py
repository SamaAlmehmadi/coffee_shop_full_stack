import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
import sys

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)
#db_drop_and_create_all()

@app.after_request
def after_request(response):
    response.headers.add ('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add ('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTION')
    return response 



'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
# db_drop_and_create_all()

# ROUTES
'''
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
'''
#get the menu from drinks 
@app.route('/drinks', methods=['GET' ])
def getDrink():
    drinks = Drink.query.all()
    drink = [drink.short() for drink in drinks]
  
    return jsonify({      
           "success": True,
         "drinks": drink
        })
   

'''
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
'''
@app.route('/drinks-detail' ,methods=['GET'] )
def getDrinkDerail():
     drinks = Drink.query.all()
     drink = [drink.long() for drink in drinks]
    
     return jsonify({      
           "success": True,
         "drinks": drink
        })

'''
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
'''
@app.route('/drinks',methods=['POST'])
@requires_auth('post:drinks')
def createDrinks(payload):
 
    data =request.get_json()
    
    title = data.get('title')
    recipe = data.get('recipe')
    new_recipe=json.dumps(recipe)
    drink = Drink (title =title , recipe=new_recipe)
    drink.insert()
  
    return jsonify({
         "success": True, 
         "drinks":drink.long()
     })
    

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
'''
@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def editDrinks(paylaod, id):
    drink_one = Drink.query.filter(Drink.id == id).one_or_none()
    
 
    if drink_one  is None:
        abort(404)
    data=request.get_json()
    # print("what the ha", data)
    # sys.exit()
    try: 
     title = data.get('title')
     recipe = data.get('recipe')

     new_recipe = json.dumps(recipe)
     
     drink_one.title=title
     drink_one.recipe =new_recipe
     
     drink_one.update()
     
     return jsonify({
         "success": True,
          "drinks":drink_one.long()
     })

    except : 
        abort(422)


'''
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
   
'''
@app.route('/drinks/<int:id>' , methods=['DELETE'])
@requires_auth('delete:drinks')
def deleteDrink(paylaod, id):
    drink = Drink.query.filter(Drink.id == id).one_or_none()
  
    if drink is None:
        abort(404)
    drink.delete()
    return jsonify({
        "success": True, 
        "delete": drink.id
    })
# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422



@app.errorhandler(400)
def  bad_request(error):
    return jsonify({
        "success":False,
        "message": "Bad request",
        "error": 400
      }),400
'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def not_found_404(error):
     return jsonify({
       'success':False,
       'message': 'Resource Not Found',
       'error':404

     }),404

@app.errorhandler(500)
def server_error_500(error):
    return jsonify({
        'success':False,
        'message':"server error",
        'error':500
      }),500

