from django.urls import path
from . import views

urlpatterns = [
      path("", 
        views.get_api, 
        name='get_api'),
      path("deeplearning", 
         views.get_deeplearning_code, 
         name = "get_deeplearning_code"),
      path("machinelearning", 
         views.get_machinelearning_code, 
         name = "get_machinelearning_code"),
      path("report",
         views.show_report, 
         name = "show_report"),
      path("contact",
         views.get_contact, 
         name = "get_contact"),
     
   
   
 ]