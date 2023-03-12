from project.dao.model.favoritemovie import FavoriteMovies


class FavoriteMoviesDAO:
    def __init__(self, session):
        self.session = session

    def create_favorites_movies(self, data):
        ent = FavoriteMovies(**data)
        self.session.add(ent)
        self.session.commit()
        return ent
    
    def delete(self, uid):
        favorite = self.session.query(FavoriteMovies).filter(FavoriteMovies.movie_id == uid).one()
        self.session.delete(favorite)
        self.session.commit()

    def get_all(self):
        return self.session.query(FavoriteMovies).all()
    
    def get_one(self, uid):
        return self.session.query(FavoriteMovies).get(uid)
