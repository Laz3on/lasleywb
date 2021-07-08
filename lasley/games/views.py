from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import requests
import json

url = "https://www.freetogame.com/api/games"
headers = {'Accept': 'application/json'}
# Create your views here.

def index(request):
    # gameList = {}
    resp = requests.get(url, headers)
    games = json.loads(resp.text)
    # print(games)
    # games = serializers.serialize('json', games)
    for game in games:
        gameImg = game['thumbnail']
        gameTitle = game['title']
        gameDesc = game['short_description']
        gameGenre = game['genre']
        gamePlatform = game['platform']
        gameReleaseDate = game['release_date']
        gameURL = game['game_url']
        gameDeveloper = game['developer']
        gameList = dict(Image=gameImg,Title=gameTitle,Desc=gameDesc,Genre=gameGenre,Platform=gamePlatform,ReleaseDt=gameReleaseDate,URL=gameURL,Developer=gameDeveloper)

        context = {
            'gameImg':gameImg,
            'title':gameTitle,
            'desc':gameDesc,
            'genre':gameGenre,
            'platform':gamePlatform,
            'release_Date':gameReleaseDate,
            'url':gameURL,
            'developer':gameDeveloper,
        }
    # return(gameList)
        # print(gameList)
    # return render_to_response('games.html', gamesList.items())
    return render(request, 'games.html', context=context)
