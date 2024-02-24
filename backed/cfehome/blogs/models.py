from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=155)
    content = models.TextField(blank=True, null=True)
    