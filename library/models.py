from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DR", 'Draft'
        PUBLISHED = "PB", 'Published'
        REJECTED = "RJ", 'Rejected'


    title = models.CharField(max_length=250)
    author = models.CharField(max_length=205)
    price = models.IntegerField(default=0)
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField()
    genre = models.CharField(max_length=250)
    number_of_pages = models.IntegerField(default=0)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published']),
        ]
    def __str__(self):
        return self.title
