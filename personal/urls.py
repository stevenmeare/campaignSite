from django.urls import path, include
from . import views

app_name='personal'
urlpatterns = [
    path('', views.index, name='index'),
    
]