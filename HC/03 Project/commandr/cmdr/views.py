from django.views.generic import ListView

from .models import abc
# Create your views here.

class HomePageView(ListView):
	model = abc
	template_name = 'home.html'