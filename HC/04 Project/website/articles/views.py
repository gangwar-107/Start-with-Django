from django.views.generic import ListView,DetailView

# Create your views here.

from .models import Articles

class ArticlesPageView(ListView):
	model = Articles
	template_name = 'home.html'

class ArticlesDetailView(DetailView):
	model = Articles
	template_name = 'details.html'
	context_object_name = 'batman'



