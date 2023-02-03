import json
import requests

from django.shortcuts import render

def get_api(request) :
    url = 'http://43.200.179.186/'
    res = requests.get(url)
    text = res.json()
    return render(request,'index.html',{"text":text})
        
