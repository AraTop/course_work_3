from flask import Flask
from flask_restx import Api
from project.config import Config
from project.dao.model.director import Director
from project.dao.model.genre import Genre
from project.dao.model.movie import Movie
from project.dao.model.user import User
from project.setup.db import db
from project.views.directors import director_ns
from project.views.genres import genre_ns
from project.views.movies import movie_ns
from project.views.user import user_ns
from project.views.auth import auth_ns
from project.views.favorites import favorites_ns
from project.load_json import data

def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    register_extensions(application)

    return application

def create_tables(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        movies = [Movie(**one) for one in data["movies"]]
        db.session.add_all(movies)

        directors = [Director(**one) for one in data["directors"]]
        db.session.add_all(directors)

        genres = [Genre(**one) for one in data["genres"]]
        db.session.add_all(genres)

        db.session.commit()

def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(favorites_ns)
    create_tables(application)

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run(host="localhost", port=10001, debug=True)
