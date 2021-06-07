from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('greeting/<int:num>', views.dingusgreet)
    
]
