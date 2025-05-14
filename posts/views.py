from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    """
    We will list the contents of our database model
    on a HTML template homepage
    """

    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

