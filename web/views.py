import json
import requests

from django.shortcuts import render, get_object_or_404, redirect

def get_api(request) :
    return render(request,'index.html')

def get_code(request) :
    return render(request, 'code.html')
        
