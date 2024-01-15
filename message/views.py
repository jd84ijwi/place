from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
import message

from .forms import MessageMessageForm
from .models import Message

@login_required
def new_message(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index') 

    message_list = Message.objects.filter(item=item).filter(members__in=[request.user.id])

    if message_list.exists():
        return redirect('some_message_url', pk=message_list.first().pk)  

    form = MessageMessageForm()

    if request.method == 'POST':
        form = MessageMessageForm(request.POST)

        if form.is_valid():
            message_instance = Message.objects.create(item=item)
            message_instance.members.add(request.user, item.created_by)

            message_content = form.save(commit=False)
            message_content.message = message_instance
            message_content.created_by = request.user
            message_content.save()

            return redirect('item:detail', pk=item_pk)

    return render(request, 'message/new.html', {'form': form})


@login_required
def inbox(request):
    messages = Message.objects.filter(members__in=[request.user.id]) 
    
    return render(request, 'message/inbox.html', {'messages': messages})


@login_required
def detail(request, pk):
    current_message = get_object_or_404(Message, pk=pk, members__in=[request.user.id])

    form = MessageMessageForm()

    if request.method == 'POST':
        form = MessageMessageForm(request.POST)

        if form.is_valid():
            message_content = form.save(commit=False)
            message_content.message = current_message
            message_content.created_by = request.user
            message_content.save()

            return redirect('message:detail', pk=pk)

    return render(request, 'message/detail.html', {'message': current_message, 'form': form})