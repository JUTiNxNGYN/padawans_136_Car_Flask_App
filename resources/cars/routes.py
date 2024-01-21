from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import PostModel
from schemas import PostSchema, PostSchemaNested

from . import bp
# post routes

@bp.route('/<car_id>')
class Post(MethodView):

  @bp.response(200, PostSchemaNested)
  def get(self, car_id):
    post = PostModel.query.get(car_id)
    if post:
      print(post.author)
      return post 
    abort(400, message='Invalid Car')

  @bp.arguments(PostSchema)
  def put(self, car_data ,car_id):
    post = PostModel.query.get(car_id)
    if post:
      post.body = car_data['body']
      post.commit()   
      return {'message': 'Car updated'}, 201
    return {'message': "Invalid Car Id"}, 400
    

  def delete(self, car_id):
    post = PostModel.query.get(car_id)
    if post:
      post.delete()
      return {"message": "Car Deleted"}, 202
    return {'message':"Invalid Car"}, 400

@bp.route('/')
class PostList(MethodView):

  @bp.response(200, PostSchema(many = True))
  def get(self):
    return PostModel.query.all()
  
  @bp.arguments(PostSchema)
  def post(self, car_data):
    try:
      post = PostModel()
      post.user_id = car_data['user_id']
      post.body = car_data['body']
      post.commit()
      return { 'message': "Car Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401