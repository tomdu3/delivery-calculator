from django.contrib import admin
from django.urls import path, include

# addded paths for the app django app delivery
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('delivery.urls')),
]
