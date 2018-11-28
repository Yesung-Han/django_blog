# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post
# Register your models here.

#(1) -> decorator code 
#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    #serch in title and content 
    search_fields = ('title','content',)
    #slug prescribed using 
    prepopulated_feilds = {'slug' :('title',)}

#(1)
admin.site.register(Post, PostAdmin)
