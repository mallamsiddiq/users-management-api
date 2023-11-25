# users/models.py
from django.db import models
from authapp.models import User

class Geo(models.Model):
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    geo = models.OneToOneField(Geo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.address
    
    @property
    def address(self):
        return f'{self.street}, {self.city} | {self.suite}'
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    catchPhrase = models.CharField(max_length=255)
    bs = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'

class Profile(User):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='users')
    phone = models.CharField(max_length=20)
    website = models.URLField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users')

    def __str__(self) -> str:
        return f'{self.name}'
