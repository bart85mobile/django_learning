from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('external_entities/', views.external_entities, name='external_entities'),
    path('external_entities/update/<company_name_id>', views.external_entities_upd, name='external_entities_upd'),
    path('external_entities/delete/<company_name_id>', views.external_entities_del, name='external_entities_del'),
    path('internal_entities/', views.internal_entities, name='internal_entities'),
    path('internal_entities/update/<company_name_id>', views.internal_entities_upd, name='internal_entities_upd'),
    path('internal_entities/delete/<company_name_id>', views.internal_entities_del, name='internal_entities_del'),
    path('contracts/', views.contracts, name='contracts'),
]
