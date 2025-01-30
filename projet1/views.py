from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
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

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = UserCreationForm()
    return render(request,"register.html", {"form" : form})