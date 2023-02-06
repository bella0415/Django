from django.urls import path
from . import views

urlpatterns = [
     path("", 
        views.get_api, 
        name='get_api'),
     path("code", 
         views.get_code, 
         name = "get_code"),
     path("contact", # pk라는 int 형 변수 가 들어 감
         views.get_contact, 
         name = "get_contact"),
   
   
 ]