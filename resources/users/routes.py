from flask import request
from uuid import uuid4
from flask.views import MethodView

from . import bp
from db import users

from schemas import UserSchema
# user routes

@bp.route('/user/<user_id>')
class User(MethodView):

  @bp.response(200, UserSchema)
  def get(self,user_id):
    try:
      return users[user_id]  
    except:
      return {'message': 'invalid user'}, 400
    
  @bp.arguments(UserSchema)
  def put(self, user_data, user_id):
    try:
      user = users[user_id]
      user |= user_data
      return { 'message': f'{user["username"]} updated'}, 202
    except KeyError:
      return {'message': "Invalid User"}, 400

  def delete(self, user_id):
    try:
      del users[user_id]
      return { 'message': f'User Deleted' }, 202
    except:
      return {'message': "Invalid username"}, 400

@bp.route('/user')
class UserList(MethodView):

  @bp.response(200, UserSchema(many = True))
  def get(self):
   return list(users.values())
  
  @bp.arguments(UserSchema)
  def post(self, user_data):
    users[uuid4()] = user_data
    return { 'message' : f'{user_data["username"]} created' }, 201
    