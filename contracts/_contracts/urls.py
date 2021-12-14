from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contracts/', views.contracts, name='contracts'),
    path('external_companies/', views.external_companies, name='external_companies'),
    path('internal_companies/', views.internal_companies, name='internal_companies'),
]