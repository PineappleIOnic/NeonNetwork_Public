from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('invgen/', include('InvGen.urls')),
    path('a/', include('users.urls')),
    path('', include('pages.urls')),
    path('CDN/', include('FileHandler.urls'))
]
