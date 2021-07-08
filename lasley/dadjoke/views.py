from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import requests
import json

url = "https://www.freetogame.com/api/games"
headers = {'Accept': 'application/json'}
# Create your views here.


def index(request):
    return HttpResponse("Dad Joke")


def hello(request):
    return HttpResponse("Hello")
