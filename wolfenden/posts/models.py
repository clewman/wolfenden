# posts/models.py
from django.db import models


class Urban(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='urban/')

    def __str__(self):
        return self.title

class Nature(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='nature/')

    def __str__(self):
        return self.title

class Portrait(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='portrait/')

    def __str__(self):
        return self.title
