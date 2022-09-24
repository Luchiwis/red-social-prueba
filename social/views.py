from django.shortcuts import render
from .models import *



# Create your views here.
def feed(request):
    posts = Post.objects.all()
    ctx = {'posts':posts}

    return render(request, 'social/feed.html', ctx)

def profile(request):
    return render(request, 'social/profile.html')