from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from users.models import Profile
import random


# Create your views here.

def index(request):
    try: 
        posts= Post.objects.all()
        posts = posts[::-1]
        one_post = random.randint(0, len(posts) -1)
        random_post= posts[one_post]
        print(random_post)
    except Post.DoesNotExist:
        posts = None

    return render(request, 'index.html', locals())


