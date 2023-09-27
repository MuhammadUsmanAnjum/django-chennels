from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255)
    
    
class Message(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)