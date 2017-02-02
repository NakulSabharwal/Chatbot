import requests
from bs4 import BeautifulSoup as BS
import os

from google import search

def GoogleIt(query):
	#arr=[]
	temp =""
	#url ='https://www.google.co.in/?client=safari&channel=mac_bm&gws_rd=cr&ei=s9-SWKShA4T2vAT3r5uICQ#channel=mac_bm&q='+query
	for url in search(str(query), tld='com.pk', lang='es', stop=5):
	    temp = temp +'\n' +url
	return temp
    
#print GoogleIt(query="google")
