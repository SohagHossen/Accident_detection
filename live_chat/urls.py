from django.urls import path
from. import views
urlpatterns = [
    path('', views.GroupChat, name='GroupChat'),
]
