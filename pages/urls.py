from django.urls import path
import django
from .views import HomePageView, AboutPageView, NoPageView, HomeMobilePageView, SettingsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('mobile/', HomeMobilePageView.as_view(), name='mobileHome'),
    path('settings/', SettingsView.as_view(), name='DesktopSettings')
]
