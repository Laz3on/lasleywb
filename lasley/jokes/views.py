from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json

url = "https://icanhazdadjoke.com/"
chuck_url = "https://api.chucknorris.io/jokes/random"
headers = {"Accept": "application/json"}
# Create your views here.


def jokes(request):
    resp = requests.get(url, headers=headers)
    joke = json.loads(resp.text)
    joke = joke["joke"]

    response = requests.get(chuck_url, headers=headers)
    norris = json.loads(response.text)
    norris = norris["value"]

    template = loader.get_template("jokes.html")
    return HttpResponse(template.render({"joke": joke, "norris": norris}, request))
