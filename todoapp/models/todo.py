from django.db import models
from django.utils import timezone

class Todo(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title