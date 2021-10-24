from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
import requests
import json

url = "https://www.freetogame.com/api/games"
headers = {"Accept": "application/json"}

games_by_platform_url = "https://www.freetogame.com/api/games?platform=pc"

# Create your views here.


def index(request):
    resp = requests.get(url, headers)
    games = json.loads(resp.text)
    return render(request, "games.html", {"games": games})


def games_by_platform(request):
    pass
