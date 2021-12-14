from django.contrib import admin
from django.urls import path, include
from _contracts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('_contracts.urls')),
]
