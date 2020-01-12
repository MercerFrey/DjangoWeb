# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length =100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default = 'default.png', blank = True)
    #author

    """
    when make a change in migrations typ these :
        python manage.py makemigrations
        python manage.py migrate
    """

    # toString in python
    def __str__(self):
        return self.title

    # gösterirken kısaltılmış halini gösteriyor.
    def snippet(self):
        return self.body[:50] + " ... "
