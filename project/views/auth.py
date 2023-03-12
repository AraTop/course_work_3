from flask import request
from flask_restx import Resource, Namespace
from project.container import auth_service , user_service

auth_ns = Namespace('auth')

@auth_ns.route("/register")
class AuthRegister(Resource):
   def post(self):
      data = request.json
      if data:
         try:
            email = data.get("email")
            password = data.get("password")
         
            if None in [email , password]:
               return "", 400

            auth_service.create_user(email, password)
            return "", 201
         
         except Exception as s:
            return str(s), 404

@auth_ns.route("/login")
class AuthLogin(Resource):
   def put(self):
      data = request.json
      if data:
         try:
            email = data.get("email")
            password = data.get("password")

            tokens = auth_service.create_tokens(email,password)
            return tokens, 201
         except Exception as s:
            return str(s)