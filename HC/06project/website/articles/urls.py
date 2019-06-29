
from django.urls import path

from . import views

urlpatterns = [
    path('',views.ArticlesPageView.as_view(), name='home'),
    path('articles/<int:pk>',views.ArticlesDetailView.as_view(),name = 'article_page'),
    path('articles/new',views.ArticlesCreateViews.as_view(),name='new_article'),
    path('articles/<int:pk>/edit',views.ArticlesUpdateView.as_view(),name='update_article'),
    path('articles/<int:pk>/delete',views.ArticleDeleteView.as_view(),name='delete_article'),

]