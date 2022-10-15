from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import UserRegisterForm



# Create your views here.
def feed(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}

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