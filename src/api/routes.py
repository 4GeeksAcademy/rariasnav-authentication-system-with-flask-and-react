"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = list(map(lambda user: user.serialize() , all_users))

    return jsonify(result)

@api.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    
    return jsonify(user.serialize()), 200

@api.route('/signup', methods=['POST'])
def add_user():
    body = request.get_json()
    user = User.query.filter_by(email=body['email']).first()

    if user != None:
        return jsonify({'msg' : 'email already in use'})

    if user == None:
        user = User(
            email = body['email'],
            password = body['password'],
            is_active = True
        )
        db.session.add(user)
        db.session.commit()

        response_body = {
            'msg' : 'user created succcesfully'
        }

        return jsonify(response_body), 200
    

@api.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    body = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    updating_email = User.query.filter_by(email = body['email']).first()

    if user != None:
        return jsonify({'msg' : 'email already in use'})

    if updating_email == None:
        user.email = body['email']
        user.password = body['password']

        db.session.commit()

        response_body = {
            'msg' : 'user updated succesfully'
        }

        return jsonify(response_body), 200
    

@api.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()

    response_body = {
        'msg' : 'user deleted succesfully'
    }
    return jsonify(response_body), 200
