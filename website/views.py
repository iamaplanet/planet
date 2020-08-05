from django.shortcuts import render
from .models import Costumer
from .forms import CostumerForm

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def register(request):
    if request.method == "POST":
        form = CostumerForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {})
        else:
            return render(request, 'register.html', {})

    else:
        return render(request, 'register.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def people(request):
    return render(request, 'people.html', {})