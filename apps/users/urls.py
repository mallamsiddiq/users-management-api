# users/urls.py
from django.urls import path
from .views import UserListCreateView, CompanyListView, AddressListView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('address/', AddressListView.as_view(), name='address-list'),

]
