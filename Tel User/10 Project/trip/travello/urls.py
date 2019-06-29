from travello.views import indexView
from django.urls import path,include
from django.conf.urls import url


urlpatterns = [
   path('',indexView,name = 'home'),
]
