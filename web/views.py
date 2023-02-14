import json
import requests

from django.shortcuts import render, get_object_or_404, redirect

# email 전송
from django.core.mail import EmailMessage

# api 호출 페이지
def get_api(request) :
    return render(request,'index.html')

# 딥러닝 코드 페이지 
def get_deeplearning_code(request) :
    return render(request, 'deep_learning_code.html')

# 머신러닝 코드 페이지 
def get_machinelearning_code(request) :
    return render(request, 'machine_learning_code.html')

# 리포트 페이지
def show_report(request) :
    return render(request, 'report.html')

# contact 페이지      
def get_contact(request) :
    return render(request, 'contact.html')

