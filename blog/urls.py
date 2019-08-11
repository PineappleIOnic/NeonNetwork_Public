from django.urls import path
from . import views

urlpatterns = [
	path('', views.blog_index, name='BlogIndex'),
	path('admin/', views.blog_admin, name='BlogAdmin'),
	path('post/<int:id>', views.blog_viewpost),
]
