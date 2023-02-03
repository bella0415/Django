from django.shortcuts import render
import requests

def web_test(request) :
    url = 'http://43.200.179.186/'
    res = requests.get(url)
    text = res.json()
    
    if text == None :
        return render(request,'index.html')
    else :
        return render(request, 'index.html',{"text":text})

