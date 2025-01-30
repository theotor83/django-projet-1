from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
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
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.infos(request, 'Password is not the same')
            return redirect('register')
    else:
        return render(request,'register.html')