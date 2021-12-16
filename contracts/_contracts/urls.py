from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contracts/', views.contracts, name='contracts'),
    path('business_entities/', views.business_entities, name='business_entities'),
]