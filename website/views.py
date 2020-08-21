from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import Costumer, Invitation, Invitee
from .forms import CostumerForm, InvitationForm, InviteeForm
from django.contrib import messages
import datetime
import random


# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def register(request):
    Date = datetime.datetime.now()
    Date_ = Date.strftime("%Y-%m%d-%H%M-%S")
    n = random.randint(10,99)
    application_number = Date_ + str(n)

    if request.method == "POST":
        form = CostumerForm(request.POST or None)
        if request.POST['event']=='error':
            application_number = request.POST['application_number']
            from_kakching = request.POST['from_kakching']
            event = request.POST['event']
            messages.success(request, ('Please select an event...'))
            return render(request, 'register.html', {'application_number':application_number,'from_kakching': from_kakching,'event': event})
        elif form.is_valid():
            application_number = request.POST['application_number']
            form.save()
            return render(request, 'invitation.html', {'application_number':application_number})
        else:
            application_number = request.POST['application_number']
            host_name = request.POST['host_name']
            mobile_number = request.POST['mobile_number']
            email = request.POST['email']
            from_kakching = request.POST['from_kakching']
            address = request.POST['address']
            event = request.POST['event']
            event_date = request.POST['event_date']
            messages.success(request, ('There was an error in your form! Please try again...'))
            return render(request, 'register.html', {'application_number':application_number,
                'host_name': host_name,
                'mobile_number': mobile_number,
                'email': email,
                'from_kakching': from_kakching,
                'address': address,
                'event': event,
                'event_date': event_date,
            })

    else:
        return render(request, 'register.html', {'date':application_number})

def eventView(request, evnt):
    Date = datetime.datetime.now()
    Date_ = Date.strftime("%Y-%m%d-%H%M-%S")
    n = random.randint(10,99)
    application_number = Date_ + str(n)

    if request.method == "POST":
        form = CostumerForm(request.POST or None)
        if form.is_valid():
            application_number = request.POST['application_number']
            form.save()
            return render(request, 'invitation.html', {'application_number':application_number})
        else:
            application_number = request.POST['application_number']
            host_name = request.POST['host_name']
            mobile_number = request.POST['mobile_number']
            email = request.POST['email']
            from_kakching = request.POST['from_kakching']
            address = request.POST['address']
            event_date = request.POST['event_date']
            messages.success(request, ('There was an error in your form! Please try again...'))
            return render(request, 'register.html', {'application_number':application_number,
                'host_name': host_name,
                'mobile_number': mobile_number,
                'email': email,
                'from_kakching': from_kakching,
                'address': address,
                'event_date': event_date,
            })

    else:
        return render(request, 'registerEvent.html', {'evnt':evnt, 'date':application_number})

def contact(request):
    return render(request, 'contact.html', {})

def status(request):
    if request.method == "POST":
        application_number = request.POST.get('application_number')
        host = Costumer.objects.get(application_number=application_number)
        return redirect('dashboard', appliNo=application_number)
    return render(request, 'status.html', {})

def invitation(request):
    if request.method == "POST":
        application_number = request.POST.get('application_number')
        invitation = request.POST.get('invitation')
        host = Costumer.objects.get(application_number=application_number)
        data = {'host':host,'invitation':invitation}
        form = InvitationForm(data)
        if form.is_valid():
            form.save()
            return render(request, 'people.html', {'application_number':application_number})
        else:
            return render(request, 'invitation.html', {'msg':form.errors,'invitation':invitation,'host':host})
    return render(request, 'invitation.html', {})

def people(request):
    if request.method == "POST":
        application_number = request.POST.get('application_number')
        nameList = request.POST.getlist('name')
        mobile_noList = request.POST.getlist('mobile_no')
        addressList = request.POST.getlist('address')
        host = Costumer.objects.get(application_number=application_number)
        InviteeList = []
        i = 0
        for name in nameList:
            invitee = {'host':host, 'name':name, 'mobile_no':mobile_noList[i], 'address':addressList[i]}
            InviteeList.append(invitee)
            i = i+1
        for invitee in InviteeList:
            form = InviteeForm(invitee)
            if form.is_valid():
                form.save()
            else:
                return render(request, 'people.html', {'msg':form.errors})
        return redirect('dashboard', appliNo=application_number)
    return render(request, 'people.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def dashboard(request, appliNo):
    host = Costumer.objects.get(application_number=appliNo)
    invitees = Invitee.objects.get_queryset().filter(host=host)
    return render(request, 'dashboard.html', {"host":host, "invitees":invitees})