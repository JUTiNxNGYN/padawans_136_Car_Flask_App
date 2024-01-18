from flask import request
from uuid import uuid4

from app import app
from db import cars, users

@app.get('/cars')
def carList():
    return {'cars':cars}

@app.get('/cars/<car_name>')
def carSpec(car_name):
    try:
        return {f'{car_name}':cars[car_name]},200
    except KeyError:
        return {"message": "Invalid car"}, 400


@app.post('/cars')
def add_car():
    car_data = request.get_json()   
    user_id = car_data['user_id']
    if user_id in users:
        cars[uuid4()]= car_data
        return { 'message': "Car Created" }, 201
    return { 'message': "Invalid User"}, 401

@app.put('/car/<car_id>')
def update_car(car_id):
    try:
        post = cars[car_id]
        post_data = request.get_json()
        if post_data['user_id']== post['user_id']:
            post['body'] = post_data['body']
            return {'message': 'Car Updated'}, 202
        return {'message': "Unauthorized"}, 401
    except:
        return{'message': "Invalid Post"}, 400
    
@app.delete('/car/<car_id>')
def delete_car(car_id):
    try:
        del cars[car_id]
        return {"message": "Car Deleted"}, 202
    except:
        return {'message': "Invalid Car"}, 400