import calendar
import datetime
from flask import abort
from project.constants import JWT_SECRET , JWT_ALGORITHM
from project.services.user import UserService
import jwt

class AuthService:
   def __init__(self, user_service: UserService):
      """создание user_service для того чтоб его испольовать для получение пользователя при создание токена"""

      self.user_service = user_service

   def create_user(self, email, password):
      """праверка подлиности пороля, именни , создание токеноф, польователя"""

      try: 
         data_user = {
         "email": email,
         "password":password
         }
         self.user_service.create(data_user)

      except Exception as s:
         return str(s)


   def create_tokens(self, email, password ):
      """создаем пару токенов"""
      
      user = self.user_service.get_by_user(email)

      if not user:
         abort(401)

      if not self.user_service.compare_passwords(user.password , password):
         abort(401)

      data = {

         "username": user.name,
         "id":user.id
      }
      
      #создание на 30 мин access_token
      min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
      data["exp"] = calendar.timegm(min30.timetuple())
      access_token = jwt.encode(data , JWT_SECRET , algorithm=JWT_ALGORITHM)
      #создание на 130 дней refresh_token
      days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
      data["exp"] = calendar.timegm(days130.timetuple())
      refresh_token = jwt.encode(data , JWT_SECRET , algorithm=JWT_ALGORITHM)

      return {

         "access_token": access_token,
         "refresh_token": refresh_token
      }


