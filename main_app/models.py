from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail', kwargs={'pk': self.id})


class DVD(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    release_year = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(blank=True)

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='dvds')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dvd-detail', kwargs={'pk': self.id})