# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post
# Create your views here.

class PostLV(ListView):
    model = Post
    #html file name
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'

    #automatically use django pagenation
    #one page show 2 object
    paginate_by = 2

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    #latest object shows first
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'
class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'



