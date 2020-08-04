from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('register.html', views.register, name='register'),
    path('contact.html', views.contact, name='contact'),
    path('people.html', views.people, name='people'),
]