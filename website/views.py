from django.shortcuts import render
import requests

def web_test(request) :
    url = 'http://43.200.179.186/'
    res = requests.get(url)
    text = res.json()
    return render(request, 'index.html',{"text":text})

