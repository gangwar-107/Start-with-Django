from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homeView,name = 'home'),
    path('secret/',views.secret_page, name = 'secret'),
    path('secret2/',views.SecretPage.as_view(),name='secret2'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',views.signup, name = 'signup')
    
]