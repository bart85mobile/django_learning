from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contracts/', views.contracts, name='contracts'),
    path('business_entities/', views.business_entities, name='business_entities'),
    path('business_entities/update/<company_name_id>', views.business_entities_upd, name='business_entities_upd'),
    path('business_entities/delete/<company_name_id>', views.business_entities_del, name='business_entities_del'),
]
