from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blogging.models import Author, Post


class BlogListView(ListView):
    context_object_name = "author"
    queryset = Author.objects.all()


class BlogDetailView(DetailView):
    context_object_name = "post"
    queryset = Post.objects.order_by("-published_date")
