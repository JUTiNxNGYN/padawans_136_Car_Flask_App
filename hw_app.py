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

@app.get('/user')
def user():
    return { 'users': list(users.values()) }, 200

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

@app.post('/cars')
def create_post():
    post_data = request.get_json()   
    user_id = post_data['user_id']
    if user_id in users:
        cars[uuid4()]= post_data
        return { 'message': "Post Created" }, 201
    return { 'message': "Invalid User"}, 401

@app.put('/post/<post_id>')
def update_post(post_id):
    try:
        post = cars[post_id]
        post_data = request.get_json()
        if post_data['user_id']== post['user_id']:
            post['body'] = post_data['body']
            return {'message': 'Post Updated'}, 202
        return {'message': "Unauthorized"}, 401
    except:
        return{'message': "Invalid Post"}, 400
    
@app.delete('/post/<post_id>')
def delete_post(post_id):
    try:
        del cars[post_id]
        return {"message": "Post Deleted"}, 202
    except:
        return {'message': "Invalid Post"}, 400

