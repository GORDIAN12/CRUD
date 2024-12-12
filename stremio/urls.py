from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('',views.index, name="index"),
    path('about', views.about, name="about"),
    path('clients', views.clients, name="clients"),
    path('clients/create', views.create, name="create"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('clients/edit/<int:id>', views.edit, name="edit"),
    path('logout/', exit, name='exit'),
    ]
