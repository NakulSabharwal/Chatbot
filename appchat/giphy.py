import requests
import json

url = 'funny+cat&api_key=dc6zaTOxFJmzC'

def get_gif(query):
	url = 'http://api.giphy.com/v1/gifs/search?q='+query+'&api_key=dc6zaTOxFJmzC'