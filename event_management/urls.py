from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('events.urls')),
    # path('dashboard/', include('events.urls')),

] + debug_toolbar_urls()
