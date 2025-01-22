from django.http import HttpResponse
from django.shortcuts import render
from .models import TodoEntry


# Create your views here.
def index(request):
    if request.method == 'POST':
        entryName = request.POST.get('newEntry')
        newEntry = TodoEntry
        newEntry.name = entryName
        newEntry.save()
        return render(request, 'index.html',{'test': entry})
    else:
        return render(request, 'index.html')

def print(request):
    caca = request.POST['pseudo']
    return render(request, 'print.html',{'caca': caca})

def utf(request):
    return render(request, 'index_utf.html')

def test(request):
    if request.method == 'POST':
        test = request.POST.get('bouton')
        return render(request, 'test.html', {'test': test})
    return render(request, 'test.html')