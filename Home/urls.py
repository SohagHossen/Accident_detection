from django.urls import path
from. import views
urlpatterns = [
    path('', views.Home, name='home'),
    path('base', views.Base, name='base'),


]
