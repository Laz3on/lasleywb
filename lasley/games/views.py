from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.core.paginator import Paginator
import requests
import json

url = "https://www.freetogame.com/api/games"
headers = {"Accept": "application/json"}
# Create your views here.


def index(request):
    gameList = {}
    resp = requests.get(url, headers)
    games = json.loads(resp.text)
    # games = games[10]
    # print(games)
    paginator = Paginator(games, 25)

    # page_number = request.Get.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request, "games.html", {"games": games})
    # return HttpResponse(games)
