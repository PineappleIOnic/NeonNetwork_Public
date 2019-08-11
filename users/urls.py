from django.urls import path

from . import views

urlpatterns = [
    path('add/<str:friendid>', views.friend_add),
    path('accept/<str:requestid>', views.request_accept),
    path('deny/<str:requestid>', views.request_reject),
    path('unfriend/<str:requestid>', views.friend_unfriend),
]
