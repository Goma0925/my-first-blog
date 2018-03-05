
from django.urls import include, path
from . import views

urlpatterns = [
    path(r'', views.post_list, name='post_list'),
    path(r'post/new/', views.post_new, name='post_new')
]