# users/serializers.py
from collections import OrderedDict
from rest_framework import serializers
from .models import Profile, Address, Geo, Company

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat', 'lng']

class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']

class ListAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'address']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'catchPhrase', 'bs']

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = Profile
        fields = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'address', 'phone', 'website', 'company']