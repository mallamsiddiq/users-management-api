# users/views.py
from rest_framework import generics, filters
from .models import Company, Profile, Address
from .serializers import CompanySerializer
from .serializers import UserSerializer, UserCreateSerializer, ListAddressSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserSerializer


class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = ListAddressSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['street', 'city']
