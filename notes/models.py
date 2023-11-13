from typing import Any
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.id}. {self.title}'
