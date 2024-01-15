from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Category, Item

# def items(request):
#     query = request.GET.get('query', '')
#     category_id = request.GET.get('category', 0)
#     categories = Category.objects.all()
#     items = Item.objects.filter(is_sold = False)

#     if category_id:
#         items = items.filter(category__id=category_id)

#     if query:
#         items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

#     return render(request, 'item/items.html', {
#         'item': items,
#         'query': query,
#         'categories': categories,
#         'category_id': int(category_id),
#     })

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    #category id comes back as string if it exists, but integer if not
    #we need to change it to to int no matter what
    try:
        category_id = int(category_id)
    except ValueError:
        category_id = 0  #make category 0 if the string doesn't represent a number

    if category_id > 0:  # Assuming 0 means 'all categories'
        items = items.filter(category__id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,  
        'query': query,
        'categories': categories,
        'category_id': category_id,
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})

@login_required
def edit(request, pk): 
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form=EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            
            return redirect('item:detail', pk=item.id)
        
    else: 
        form = NewItemForm(instance=item)
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item'
        
        })

@login_required
def new(request): 
    if request.method == 'POST':
        form=NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            
            return redirect('item:detail', pk=item.id)
    form = NewItemForm()
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item'
        
        })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')