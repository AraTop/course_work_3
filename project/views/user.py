from flask import abort, request
from flask_restx import Resource, Namespace
import jwt
from project.constants import JWT_ALGORITHM, JWT_SECRET

from project.dao.model.user import User, UserSchema
from project.helpers.decorators import auth_required
from project.container import user_service

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        try:
            token = request.headers.get('Authorization')
            decoded_token = jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
            user_id = decoded_token.get("id")
    
        except Exception as s:
            print(s)
            abort(401)

        user = user_service.get_one(user_id)
        users_schema = UserSchema().dump(user)
        return users_schema, 200
    
    @auth_required
    def patch(self):
        req_json = request.json
        if req_json:
            try:
                token = request.headers.get('Authorization')
                decoded_token = jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
                user_id = decoded_token.get("id")
                req_json["id"] = user_id
                user_service.update(req_json, password_is=True)
                return "", 201
            except Exception as s :
                return str(s)
           
@user_ns.route('/password')
class UserView(Resource):
    @auth_required
    def put(self):
        req_json = request.json
        if req_json:
            try:
                token = request.headers.get('Authorization')
                decoded_token = jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
                user_id = decoded_token.get("id")

                password_old = req_json.get("password_old")
                password_new = req_json.get("password_new")
    
                if None in [password_old , password_new]:
                    return "", 400
                
                user = user_service.get_one(user_id)
                password_hash = user.password
                
                user_service.compare_passwords(password_hash, password_old)

                data = {
                    "id":user_id,
                    "password":password_new
                }
                user_service.update(data, password_is=False)
                return "", 201
            except Exception as s:
                return str(s)
            
            
    
        

    