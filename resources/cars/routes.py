from flask import request
from uuid import uuid4

from app import app
from db import cars, users


@app.post('/cars')
def create_car():
    post_data = request.get_json()   
    user_id = post_data['user_id']
    if user_id in users:
        cars[uuid4()]= post_data
        return { 'message': "Post Created" }, 201
    return { 'message': "Invalid User"}, 401

@app.put('/post/<post_id>')
def update_car(car_id):
    try:
        post = cars[car_id]
        post_data = request.get_json()
        if post_data['user_id']== post['user_id']:
            post['body'] = post_data['body']
            return {'message': 'Post Updated'}, 202
        return {'message': "Unauthorized"}, 401
    except:
        return{'message': "Invalid Post"}, 400
    
@app.delete('/post/<post_id>')
def delete_car(car_id):
    try:
        del cars[car_id]
        return {"message": "Car Deleted"}, 202
    except:
        return {'message': "Invalid Car"}, 400
