from django.db import models

class Book(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    path = models.CharField(max_length=255)

    class Meta:
        ordering = ('author', 'title')
        unique_together = ('author', 'title')