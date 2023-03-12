from flask import request
from flask_restx import Resource, Namespace
import jwt
from project.constants import JWT_ALGORITHM, JWT_SECRET
from project.helpers.decorators import auth_required
from project.container import user_service , favorites_service , movie_service

favorites_ns = Namespace('favorites')

@favorites_ns.route("/movies/<int:uid>")
class FavoritesMovies(Resource):
   @auth_required
   def post(self, uid):
      try:
         token = request.headers.get('Authorization')
         decoded_token = jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
         user_id = decoded_token.get("id")
         movie_id = uid
         
         if None in [user_id , movie_id]:
            return "", 400
         
         data = {
                  "user_id":user_id,
                  "movie_id":movie_id
                }
         
         data_user = {
            "id":user_id,
            "favorite_genre":movie_service.get_genre_id(movie_id)
         }
         favorites_service.create_favorites_movies(data)
         user_service.update(data_user, password_is=True)
         return "", 201
      
      except Exception as s:
         return str(s) , 404
      
   @auth_required
   def delete(self, uid):
      try:
         if uid:
            favorites_service.delete(uid)
            return "", 203
      except Exception as s:
         return str(s), 404
      