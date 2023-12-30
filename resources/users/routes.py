from flask import request
from uuid import uuid4

from app import app
from db import users

@app.get('/user')
def user():
    return { 'users': list(users.values()) }, 200

@app.get('/user/<user_id>')
def get_user(user_id):
   try:
      return { 'user: users[user_id]'}
   except:
      return {'message': 'invalid user'}, 400

@app.route('/user', methods=["POST"])
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return { 'message' : f'{json_body["username"]} created'}, 201

@app.put('/user/<user_id>')
def update_user(user_id):
  try:
    user = users[user_id]
    user_data = request.get_json()
    user |= user_data
    return { 'message': f'{user["username"]} updated'}, 202
  except KeyError:
    return {'message': "Invalid User"}, 400

@app.delete('/user/<user_id>')
def delete_user(user_id):
  try:
    del users[user_id]
    return { 'message': f'User Deleted' }, 202
  except:
    return {'message': "Invalid username"}, 400