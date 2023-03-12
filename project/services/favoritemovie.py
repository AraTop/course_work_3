from project.dao.favoritemovie import FavoriteMoviesDAO


class FavoriteMoviesService:
   def __init__(self, dao: FavoriteMoviesDAO):
      self.dao = dao

   def create_favorites_movies(self, data):
      return self.dao.create_favorites_movies(data)

   def delete(self, uid):
      return self.dao.delete(uid)
   
   def get_all(self):
      return self.dao.get_all()
    