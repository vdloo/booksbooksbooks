from django.db import models

class Book(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='Unknown Author')
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    extension = models.CharField(max_length=100)
    path = models.CharField(max_length=255)

    class Meta:
        ordering = ('-year', 'author', 'title')
        unique_together = ('author', 'title')
