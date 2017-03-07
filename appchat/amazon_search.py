import requests
from bs4 import BeautifulSoup as BS
import os

from google import search

def AmazonIt(query):
	url = "http://www.amazon.in/s/ref=nb_sb_noss_2?url=node%3D4363895031&field-keywords=" + query
	print url
	r = requests.get(url)
	html = r.text
	#print html
	soup = BS(html)

    
	h3 = soup.find_all('div',id='rightContainerATF')
	#print h3
	h2 = h3[0].find_all('div',class_='s-item-container')
	
print AmazonIt(query="iPad")
