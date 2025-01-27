from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoEntry


# Create your views here.
def index(request):
    if request.method == 'POST':
        entryName = request.POST.get('newEntry')
        newEntry = TodoEntry()
        newEntry.name = entryName
        newEntry.save()
        return redirect('/') 
    else:
        entries = TodoEntry.objects.all()
        return render(request, 'index.html', {'entries': entries})

def delete_entry(request, id):
    entry = get_object_or_404(TodoEntry, pk=id)
    entry.delete()
    return redirect('/')

def edit_entry(request, id):
    entry = get_object_or_404(TodoEntry, pk=id)
    if entry.completed == True:
        entry.completed = False
    elif entry.completed == False:
        entry.completed = True
    entry.save()
    return redirect('/')