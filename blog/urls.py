from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post

"""
    The URL config for the blog app. This file is responsible for mapping URLs to views.
    The default view for the blog app is the index view, which shows a list of all the posts.
    The index view is implemented as a ListView, that displays a list of objects.
    It is configured to display the 25 most recent posts, ordered by date.
    The detail view displays a single post, with the primary key specified in the URL.

"""

app_name='blog'
urlpatterns = [
    # Show a list of all "Post" objects
    path('',
        ListView.as_view(
            queryset=
            Post.objects.all().order_by("-date")[:25],
            template_name="blog.html"
            ),
            name='index'
        ),
    # Show entries from Post table
    path('<int:pk>/',
        DetailView.as_view(
            model = Post,
            template_name="post.html"
        )
    ),
]