from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import UserRegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def feed(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}

    #delete post
    if request.method == 'POST' and 'delete' in request.POST:
        Post.objects.filter(id=request.POST['delete']).delete()
        return redirect('feed')

    #like post
    if request.method == 'POST' and 'like' in request.POST:
        post = Post.objects.get(id=request.POST['like'])
        post.likes.add(request.user)
        post.dislikes.remove(request.user)
    
    #dislike post
    if request.method == 'POST' and 'dislike' in request.POST:
        post = Post.objects.get(id=request.POST['dislike'])
        post.dislikes.add(request.user)
        post.likes.remove(request.user)


    return render(request, 'social/feed.html', ctx)

def profile(request):
    return render(request, 'social/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Cuenta creada con exito : {username}!')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    ctx = {'form':form}
    return render(request,'social/register.html', ctx)

@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect('feed')
	else:
		form = PostForm()
	return render(request, 'social/post.html', {'form' : form })

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        # posts = Post.objects.filter(user=user)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user

    # user = get_object_or_404(User, username=username)
    # posts = Post.objects.filter(user=user)
    ctx = {'user':user, 'posts':posts}
    return render(request, 'social/profile.html', ctx)

