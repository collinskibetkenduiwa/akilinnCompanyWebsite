from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home_redirect,name='home_redirect'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('projects',views.projects,name='projects'),
    path('subsidiaries',views.subsidiaries,name='subsidiaries'),
    path('careers',views.careers,name='careers'),
    path('contact',views.contact,name='contact'),
]