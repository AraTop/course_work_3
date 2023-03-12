from flask import abort
from project.dao.model.movie import Movie

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_status(self, status):
        if str(status) == "new":
            return self.session.query(Movie).order_by(Movie.id.desc()).all()
        if str(status) == "old":
            return self.session.query(Movie).order_by(Movie.id.asc()).all()

    def get_by_page(self, page):
        if page:
            if int(page) == 1:
                return self.session.query(Movie).offset(0).limit(10).all()
            if int(page) == 2:
                return self.session.query(Movie).offset(10).limit(10).all()
            if int(page) == 3:
                return self.session.query(Movie).offset(20).limit(10).all()
        abort(404)

    def get_by_status_or_page(self,page,status):
        if [page, status]:
            if int(page) == 1 and str(status) == "new":
                return self.session.query(Movie).order_by(Movie.id.desc()).offset(0).limit(10).all()
            if int(page) == 1 and str(status) == "old":
                return self.session.query(Movie).order_by(Movie.id.asc()).offset(0).limit(10).all()
            
            if int(page) == 2 and str(status) == "new":
                return self.session.query(Movie).order_by(Movie.id.desc()).offset(10).limit(10).all()
            if int(page) == 2 and str(status) == "old":
                return self.session.query(Movie).order_by(Movie.id.asc()).offset(10).limit(10).all()
            
            if int(page) == 3 and str(status) == "new":
                return self.session.query(Movie).order_by(Movie.id.desc()).offset(20).limit(10).all()
            if int(page) == 3 and str(status) == "old":
                return self.session.query(Movie).order_by(Movie.id.asc()).offset(20).limit(10).all()
            
        abort(404)
    
    
    
    
    def get_by_year(self, val):
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def get_genre_id(self,uid):
        movie = self.get_one(uid)
        id = movie.genre_id
        return id