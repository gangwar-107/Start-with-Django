from django.shortcuts import render,redirect
from .forms import descForm
from .models import videoForm

# Create your views here.


def homeView(request):
	videoes = videoForm.objects.all()
	context = {'videoes':videoes}
	return render(request, 'index.html',context)


def vrform(request):
	if request.method == 'POST':
		form = descForm(request.POST)

		if form.is_valid():
			new_req = videoForm(videotitle = request.POST['videotitle'], videodesc = request.POST['videodesc'])
			new_req.save()
			return redirect('home')

	else:
		form = descForm()

	context = {'form':form}


	return render(request, 'vrform.html', context)

