from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import requests
import json

url = "https://icanhazdadjoke.com/"
headers = {'Accept': 'application/json'}
# Create your views here.


def dadjoke(request):
    resp = requests.get(url, headers=headers)
    joke = json.loads(resp.text)
    joke = joke['joke']
    print(joke)
    html = '<h1> %s </h1>' % joke

    return HttpResponse(html)


def hello(request):
    return HttpResponse("Hello")
