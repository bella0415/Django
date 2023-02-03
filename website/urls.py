from django.urls import path
from . import views

urlpatterns = [ 
    path("text",  # url 주소 
         views.web_test,  # 접속하면 함수 web_test 실행
         name = "web_test"), # 이름 지정 
]