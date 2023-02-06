import json
import requests

from django.shortcuts import render, get_object_or_404, redirect

# email 전송
from django.core.mail import EmailMessage

# api 호출 페이지
def get_api(request) :
    return render(request,'index.html')

# code 페이지 
def get_code(request) :
    return render(request, 'codes.html')

# contact 페이지      
def get_contact(request) :
    return render(request, 'contact.html')

