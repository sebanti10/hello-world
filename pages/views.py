#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#i.e.we’ve imported the built-in HttpResponse method 
#so we can return a response object to the user.
#Our function homePageView accepts the request object,
#returns a response with the string Hello, World!. 

def homePageView(request):
	return HttpResponse('Hello, World!')

#Basically we’re saying whenever the view function 
#homePageView is called,
#return the text “Hello, World!”