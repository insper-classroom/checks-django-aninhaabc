from typing import Any
from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f'{self.id} {self.title}'
