from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('invgen/', include('InvGen.urls')),
    path('', include('pages.urls')),
    path('CDN/', include('FileHandler.urls')),
    path('search/', include('search.urls')),
    path('friend/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('markdownx/', include('markdownx.urls')),
]

#if settings.DEBUG is True:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
