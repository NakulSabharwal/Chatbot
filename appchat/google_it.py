import requests
from bs4 import BeautifulSoup as BS
import os

from google import search

def GoogleIt(query):
	#arr=[]
	temp =""
	arr = query.split(' ')
	query = '+'.join(arr)
	print arr
	#url ='https://www.google.co.in/?client=safari&channel=mac_bm&gws_rd=cr&ei=s9-SWKShA4T2vAT3r5uICQ#channel=mac_bm&q='+query
	t = search(str(query), tld='com.in', lang='es', stop=5)
	for url in t:
	    temp = temp +'\n' +url
	return temp
    
print GoogleIt(query="google")
