from django.urls import path
from . import views
from .views import statusView, eventView

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('register.html', views.register, name='register'),
    path('contact.html', views.contact, name='contact'),
    path('people.html', views.people, name='people'),
    path('invitation.html', views.invitation, name='invitation'),
    path('status.html', views.status, name='status'),
    path('faq.html', views.faq, name='faq'),
    path('statusView.html', statusView.as_view(), name="status-details"),
    path('register/<str:evnt>', eventView, name="evnt"),
    path('dashboard/<appliNo>', views.dashboard, name='dashboard'),
]