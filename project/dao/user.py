from project.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        ent = User(**user_data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, uid):
        User = self.get_one(uid)
        self.session.delete(User)
        self.session.commit()

    def update(self, user_data):
        try:
            User = self.get_one(user_data.get("id"))
        except Exception as s:
            return str(s)
        if user_data.get("name"):
            User.name = user_data.get("name")
        if user_data.get("surname"):
            User.surname = user_data.get("surname")
        if user_data.get("favorite_genre"):
            User.favorite_genre = user_data.get("favorite_genre")
        if user_data.get("password"):
            User.password = user_data.get("password")

        self.session.add(User)
        self.session.commit()

    def get_by_user(self, email):
        return self.session.query(User).filter(User.email == email).one()
