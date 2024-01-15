from django import forms

from .models import MessageMessage

class MessageMessageForm(forms.ModelForm):
    class Meta: 
        model = MessageMessage 
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
                

            })   
        }