from django.shortcuts import render

import requests
import json

url = "https://www.freetogame.com/api/games"
headers = {'Accept': 'application/json'}
# Create your views here.

def index(request):
    # gameList = {}
    resp = requests.get(url, headers)
    json_data = json.loads(resp.text)
    games = json_data
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
        # return(gameList)

    for k, v in games:
        gameList = k, v
    return gameList
    context = gameList
    print(context)
    return render(request, 'games.html',context)
