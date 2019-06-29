from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404
from django.contrib.auth.models import User
# Create your views here.
from .models import Board,Topic,Post
from .forms import NewTopicForm
from django.contrib.auth.decorators import login_required

def home(request):
	boards = Board.objects.all()
	context = {'boards':boards}
	return render(request,'home.html',context)


def board_topics(request,pk):
	board = get_object_or_404(Board, pk=pk)
	return render(request,'topics.html',{'board':board})

@login_required
def new_topic(request,pk):
	board = get_object_or_404(Board, pk=pk)
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = request.user
			topic.save()
			post = Post.objects.create(
				message=form.cleaned_data.get('message'),
				topic=topic,
				created_by = request.user)
			return redirect('board_topics', pk= board.pk)
	else:
		form = NewTopicForm()
	

	return render(request,'new_topic.html',{'board':board,'form':form})


def topic_posts(request,pk,topic_pk):
	topic = get_object_or_404(Topic,board__pk=pk,pk=topic_pk)
	return render(request,'topic_posts.html',{'topic':topic})
