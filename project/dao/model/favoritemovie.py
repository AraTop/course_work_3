from marshmallow import Schema, fields
from project.setup.db import db

class FavoriteMovies(db.Model):
    __tablename__ = 'favorite_movies'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    user = db.relationship("User") 
    movie = db.relationship("Movie")