
from django.urls import path

from . import views

urlpatterns = [
    path('',views.ArticlesPageView.as_view(), name='home'),
    path('articles/<int:pk>',views.ArticlesDetailView.as_view(),name = 'article_page'),

]