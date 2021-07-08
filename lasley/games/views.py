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
    print(games)
    # games = serializers.serialize('json', games)
    # for game in games:
    #     gameImg = game['thumbnail']
    #     gameTitle = game['title']
    #     gameDesc = game['short_description']
    #     gameGenre = game['genre']
    #     gamePlatform = game['platform']
    #     gameReleaseDate = game['release_date']
    #     gameURL = game['game_url']
    #     gameDeveloper = game['developer']
        # gameList = gameList.append(gameImg,gameTitle,gameDesc,gameGenre,gamePlatform,gameReleaseDate,gameURL,gameDeveloper)

    return render(request, 'games.html', context=games)
    # return HttpResponse(games)
