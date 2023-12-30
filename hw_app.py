from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

users = {
    '1': {
        'username': 'JustinSmith',
        'email': 'Justinsmith@aol.com'
    },
    '2': {
        'username': 'KevinSmith',
        'email': 'Kevinsmith@aol.com'
    }
}

cars = {
    '1': {
        'Year' : '2024',
        'Make' : 'Toyota',
        'Model' : 'Tundra',
        'Trim' : 'TRD Pro',
        'Color' : 'Terra',
        'user_id' : '1'
    },
    '2': {
        'Year' : '2018',
        'Make' : 'Nissan',
        'Model' : 'GTR',
        'Trim' : 'Nismo',
        'Color' : 'Cloud White',
        'user_id' : '2'
    },
    '3': {
        'Year' : '2023',
        'Make' : 'Porsche',
        'Model' : 'Taycan',
        'Trim' : 'GTS Sport Turismo',
        'Color' : 'Chalk',
        'user_id' : '1'        
    }
}
#  CRUD (Create(GET), Read(PUT), Update, Delete)

# user routes

@app.get('/user')
def user():
  return { 'users': list(users.values()) }, 200

@app.route('/user', methods=["POST"])
def create_user():
  json_body = request.get_json()
  users[uuid4()] = json_body
  return { 'message' : f'{json_body["username"]} created' }, 201

@app.put('/user')
def update_user():
  return

@app.delete('/user')
def delete_user():
  pass

# post routes

@app.get('/post')
def get_posts():
  return

@app.post('/post')
def create_post():
  return

@app.put('/post')
def update_post():
  return

@app.delete('/post')
def delete_post():
  return