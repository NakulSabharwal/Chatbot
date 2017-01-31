from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


import requests
import json


#  Token Generated at FB EAAQqs1NbBEUBAIFw4S6k9udvHPxJKSMRrIFsCgQUt9CwEn84EuTfjKN17crolj7AfD2BZCiBjgOornxYDYqYLdckylXRQxwhBxEhcKRkrGQzxGld3RrvApWyzIZCvgchtHrpYoqJXg0kJpmhgqr5JLBOU75jP6I5wQvRuTLgZDZD

#our self made verify token
# 123456789

def mainFunc(request):
	return HttpResponse("Testing successful....")

class CommonUrl(generic.View):
	def get(self,request,*args,**kwargs):
		return HttpResponse("Hello")

class ChatBot(generic.View):
	def get(self,request,*args,**kwargs):
		print self.request.GET
		if self.request.GET.get('hub.verify_token') == '123456789':
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	def post(self,request,*args,**kwargs):
		message = json.loads(self.request.body.encode('utf-8'))

		for entry in message['entry']:
			for msg in entry['messaging']:
				print msg['message']['text']
				reply_to_message(msg['sender']['id'],msg['message']['text'])
		return HttpResponse("None")

def reply_to_message(user_id,message):
	access_token = 'EAAQqs1NbBEUBAIFw4S6k9udvHPxJKSMRrIFsCgQUt9CwEn84EuTfjKN17crolj7AfD2BZCiBjgOornxYDYqYLdckylXRQxwhBxEhcKRkrGQzxGld3RrvApWyzIZCvgchtHrpYoqJXg0kJpmhgqr5JLBOU75jP6I5wQvRuTLgZDZD'
	url = 'https://graph.facebook.com/v2.6/me/messages?access_token='+access_token

	resp = generate_response(message)
	send_resp = {"recipient":{"id":user_id},"message":{"text":resp}}
	response_msg = json.dumps(send_resp)
	status = requests.post(url,headers={"Content-Type":"application/json"},data=response_msg)
	print status.json()

def generate_response(msg):
	keywords = {
	    'help' : 'This is the help message. To use this chatbot, the list of commands'
	}	