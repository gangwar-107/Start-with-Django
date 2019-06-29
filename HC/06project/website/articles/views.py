from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

from .models import Articles

class ArticlesPageView(ListView):
	model = Articles
	template_name = 'home.html'

class ArticlesDetailView(DetailView):
	model = Articles
	template_name = 'details.html'
	context_object_name = 'batman'


class ArticlesCreateViews(CreateView):
	model = Articles
	template_name = 'new_article.html'
	fields = '__all__'


class ArticlesUpdateView(UpdateView):
	model = Articles
	template_name = 'update_article.html'
	fields = ['title','text']



class ArticleDeleteView(DeleteView):
	model = Articles
	template_name = 'delete_article.html'
	context_object_name = 'batman'
	success_url = reverse_lazy('home')