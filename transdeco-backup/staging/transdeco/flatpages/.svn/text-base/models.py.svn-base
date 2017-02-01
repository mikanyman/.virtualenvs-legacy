# -*- coding: utf-8 -*-

from django.db import models

class Flatpage(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    enable_comments = models.BooleanField()
    template_name = models.CharField(max_length=70)
    registration_required = models.BooleanField()

    class Meta:
        db_table = 'django_flatpage'
