# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

#to use revers() function 
from django.urls import reverse

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField("TITLE", max_length=50)
                                      #to replace primary key / to korean / 
    slug = models.SlugField("SLUG", 
                                   unique = True, 
                                   allow_unicode = True, 
                                   help_text = 
                                   "Fill one word to descript this post." )
                                                                #blank available
    description = models.CharField("DESCRIPTION", 
                                    max_length=100, 
                                    blank = True,
                                    help_text= "Fill description here.")

                    #text field -> provide multi line                  
    content = models.TextField("CONTENT")
                                #when Post object created time automatically saved 
    create_date = models.DateTimeField("Create Date", auto_now_add=True)
                                                #when DB save, time save
    modify_date = models.DateTimeField("Modify Date", auto_now=True)

    # Meta inner class -> to adjust options
    class Meta:
        #object name in displaied admin page
        verbose_name = 'post'
        verbose_name_plural = 'posts'

        #set table name in DB
        db_table = 'my_post'
        
        # '-' : decreament order
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    #django inner functions
    def get_absolute_url(self):
        #reverse("blog:post_detail", args = (self.slug,) -> blog/self.slug/post_detail
        return reverse("blog:post_detail", args = (self.id,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()