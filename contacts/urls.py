from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>', views.view_contact, name='view_contact'),
    path('search/', views.search, name='search'),
]