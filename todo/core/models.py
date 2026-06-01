from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False, blank=True)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.title