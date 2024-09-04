from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Managers
class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Book.Status.PUBLISHED)

# Create your models here.
class Book(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DR", 'Draft'
        PUBLISHED = "PB", 'Published'
        REJECTED = "RJ", 'Rejected'

    # relations
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_books')
    # data fields
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=205)
    price = models.IntegerField(default=0)
    description = models.TextField()
    genre = models.CharField(max_length=250)
    number_of_pages = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250)
    # date fields
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # choice fields
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    publish = PublishManager()

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published']),
        ]
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
