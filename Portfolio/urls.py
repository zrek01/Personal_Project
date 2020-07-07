from django.urls import path, include
from . import views

app_name = 'Portfolio'

urlpatterns = [
    path('', views.Resume, name = 'Resume'),

]