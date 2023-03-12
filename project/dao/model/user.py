from project.setup.db import db
from marshmallow import Schema, fields

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False, unique=True)
	password = db.Column(db.String , nullable=False)
	name = db.Column(db.String)
	surname = db.Column(db.String)
	favorite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))
	genre = db.relationship("Genre")
        
class UserSchema(Schema):
   id = fields.Int()
   email = fields.Str(nullable=False, unique=True)
   password = fields.Str(nullable=False)
   name = fields.Str()
   surname = fields.Str()
   favorite_genre = fields.Int()
   