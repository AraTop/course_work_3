from project.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        if filters.get("status") is not None and filters.get("page") is None:
            movies = self.dao.get_by_status(filters.get("status"))
        elif filters.get("page") is not None and filters.get("status") is None:
            movies = self.dao.get_by_page(filters.get("page"))
        elif filters.get("page") is not None and filters.get("status") is not None:
            movies = self.dao.get_by_status_or_page(filters.get("page"), filters.get("status"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)

    def get_genre_id(self, uid):
        return self.dao.get_genre_id(uid)