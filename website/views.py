from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Costumer
from .forms import CostumerForm
from django.contrib import messages

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
            return render(request, 'invitation.html', {})
        else:
            host_name = request.POST['host_name']
            mobile_number = request.POST['mobile_number']
            email = request.POST['email']
            from_kakching = request.POST['from_kakching']
            address = request.POST['address']
            event = request.POST['event']
            event_date = request.POST['event_date']
            description = request.POST['description']
            messages.success(request, ('There was an error in your form! Please try again...'))
            return render(request, 'register.html', {'host_name': host_name,
                'mobile_number': mobile_number,
                'email': email,
                'from_kakching': from_kakching,
                'address': address,
                'event': event,
                'event_date': event_date,
                'description': description,
            })

    else:
        return render(request, 'register.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def status(request):
    return render(request, 'status.html', {})

def people(request):
    return render(request, 'people.html', {})

def invitation(request):
    return render(request, 'invitation.html', {})

def faq(request):
    return render(request, 'faq.html', {})

class statusView(ListView):
    model = Costumer
    template_name = 'statusView.html'

def eventView(request, evnt):
    return render(request, 'registerEvent.html', {'evnt':evnt})