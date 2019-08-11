from django.urls import path
import django
from . import views

urlpatterns = [
    path('', views.HomePageView, name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('mobile/', views.HomeMobilePageView.as_view(), name='mobileHome'),
    path('settings/', views.SettingsView.as_view(), name='DesktopSettings'),
    path('terms/', views.TermsView.as_view(), name='Terms'),
    path('profile/<int:id>', views.profile_view, name='Profile'),
    path('invcheck/<str:invitecode>', views.invite_check, name='Invite_Checker'),
    path('invite/', views.invite_view.as_view(), name='Invite_Entry')
]
