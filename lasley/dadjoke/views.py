from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
import json

url = "https://icanhazdadjoke.com/"
headers = {'Accept': 'application/json'}
# Create your views here.


def dadjoke(request):
    resp = requests.get(url, headers=headers)
    joke = json.loads(resp.text)
    joke = joke['joke']
    template = loader.get_template('dadjoke.html')
    context = {
        'joke': joke
    }
    return HttpResponse(template.render(context, request))


chuck_url = "https://api.chucknorris.io/jokes/random"


def chuck(request):
    response = requests.get(chuck_url, headers=headers)
    norris = json.loads(response.text)
    norris = norris['value']
    template = loader.get_template('dadjoke.html')
    context = {
        'norris': norris
    }
    return HttpResponse(template.render(context, request))
