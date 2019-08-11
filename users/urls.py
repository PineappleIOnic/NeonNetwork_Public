from django.urls import path

from . import views

urlpatterns = [
    path('', views.invite_chk, name='index'),
]
