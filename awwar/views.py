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



class PostDetailView(DetailView):
    model = Post
    template_name = 'awwar/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'title', 'desc', 'link','technologies']
    template_name = 'awwar/post_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search(search_term)
        message = f"{search_term}"

        return render(request, 'awwar/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'awwar/search.html',{"message":message})


