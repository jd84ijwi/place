from django.contrib import admin

from .models import Message, MessageMessage 

admin.site.register(Message)
admin.site.register(MessageMessage)