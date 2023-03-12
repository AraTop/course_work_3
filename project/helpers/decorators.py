from flask import abort, request
import jwt
from project.constants import JWT_SECRET , JWT_ALGORITHM

def auth_required(func):
   def wrapper(*args, **kwargs):
      if "Authorization" not in  request.headers:
            abort(401)
        
      data = request.headers["Authorization"]
      token = data.split("bearer ")[-1]
      
      try:
         jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
         
      except Exception as s:
         print("decode", s)
         abort(401)

      return func(*args, **kwargs)
    
   return wrapper


def admin_required(func):
   def wrapper(*args, **kwargs):
      if "Authorization" not in  request.headers:
         abort(401)

      data = request.headers["Authorization"]
      token = data.split("bearer ")[-1]
      role = None
      
      try:
         user = jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
         role = user.get("role", "user")
      except Exception as s:
         print("decode", s)
         abort(401)

      if role != "admin":
         abort(403)

      return func(*args, **kwargs)
   
   return wrapper
      

