from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from .models import TodoEntry


# Create your views here.
def index(request):
    if request.method == 'POST':
        entryName = request.POST.get('newEntry')
        if request.user.is_authenticated:
            newEntry = TodoEntry(user=request.user, name=entryName)
            newEntry.save()
        else:
            messages.error(request, "You must be logged in to add tasks.")
    
    entries = TodoEntry.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'index.html', {'entries': entries})

def delete_entry(request, id):
    entry = get_object_or_404(TodoEntry, pk=id)
    entry.delete()
    if request.user.is_authenticated:
        entries = TodoEntry.objects.filter(user=request.user)
    else:
        entries = 0
    return render(request, 'index.html', {'entries': entries})

def edit_entry(request, id):
    entry = get_object_or_404(TodoEntry, pk=id)
    if entry.completed == True:
        entry.completed = False
    elif entry.completed == False:
        entry.completed = True
    entry.save()
    if request.user.is_authenticated:
        entries = TodoEntry.objects.filter(user=request.user)
    else:
        entries = 0
    return render(request, 'index.html', {'entries': entries})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.user.is_authenticated:
                entries = TodoEntry.objects.filter(user=request.user)
        else:
            entries = 0
        return render(request, 'index.html', {'entries': entries})
    else:
        form = UserCreationForm()
    return render(request,"register.html", {"form" : form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.user.is_authenticated:
                entries = TodoEntry.objects.filter(user=request.user)
        else:
            entries = 0
        return render(request, 'index.html', {'entries': entries})

    else:
        form = AuthenticationForm()
    return render(request,"login.html", {"form" : form})

def logout_view(request):
    logout(request)
    return redirect("login")