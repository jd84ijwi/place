from django.contrib.auth.models import User 
from django.db import models

from item.models import Item 

class Message(models.Model):
    item = models.ForeignKey(Item, related_name='messages', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-modified_at',)

class MessageMessage(models.Model):
    message = models.ForeignKey(Message, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='written_messages', on_delete=models.CASCADE)    

