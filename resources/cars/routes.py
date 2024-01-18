    
from flask import request
from uuid import uuid4
from flask.views import MethodView

from schemas import PostSchema
from db import cars, users
from . import bp
# post routes

@bp.route('/<car_id>')
class Post(MethodView):

  @bp.response(200, PostSchema)
  def get(self, car_id):
    try:
      return cars[car_id]
    except KeyError:
      return {'message': "Invalid Post"}, 400

  @bp.arguments(PostSchema)
  def put(self, car_data ,car_id):
    try:
      post = cars[car_id]
      if car_data['user_id'] == cars['user_id']:
        post['body'] = car_data['body']
        return { 'message': 'Car Updated' }, 202
      return {'message': "Unauthorized"}, 401
    except:
      return {'message': "Invalid Car Id"}, 400

  def delete(self, car_id):
    try:
      del cars[car_id]
      return {"message": "Car Deleted"}, 202
    except:
      return {'message':"Invalid Car"}, 400

@bp.route('/')
class PostList(MethodView):

  @bp.response(200, PostSchema(many = True))
  def get(self):
    return  list(cars.values())
  
  @bp.arguments(PostSchema)
  def post(self, car_data):
    user_id = car_data['user_id']
    if user_id in users:
      cars[uuid4()] = car_data
      return { 'message': "Car Created" }, 201
    return { 'message': "Invalid User"}, 401