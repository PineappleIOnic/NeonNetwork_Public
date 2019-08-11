from django.urls import path

from . import views

urlpatterns = [
    path('', views.invite_gen, name='index'),
]
