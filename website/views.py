from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def register(request):
    return render(request, 'register.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def people(request):
    return render(request, 'people.html', {})