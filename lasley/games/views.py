from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import requests
import json

url = "https://www.freetogame.com/api/games"
headers = {'Accept': 'application/json'}
# Create your views here.


def index(request):
    gameList = {}
    resp = requests.get(url, headers)
    games = json.loads(resp.text)
    # games = games[10]
    # print(games)

    return render(request, 'games.html', {'games':list(games)})
    # return HttpResponse(games)
