from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('Home/',include('Home.urls')),
    path('accounts/', include('allauth.urls')),
    path('chat/', include('live_chat.urls')),
    path('Live_status/', include('live_status.urls')),

]
