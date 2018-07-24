from django.urls import path

#we import path from Django to power our urlpattern

from . import views

#The period used here means reference the current 
#directory, which is our pages app containing 
#both views.py and urls.py

urlpatterns = [
    path('', views.homePageView, name='home')
]

# Our urlpattern has three parts:

#a Python regular expression for the empty string ''
#specify the view which is called homePageView
#add an optional url name of 'home'