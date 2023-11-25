 
# users/management/commands/seed_users.py
import json
from django.core.management.base import BaseCommand
from users.models import Profile, Address, Geo, Company
from urllib import request

class Command(BaseCommand):
    help = 'Seed the database with data from JSONPlaceholder API'

    def handle(self, *args, **kwargs):

        url = "https://jsonplaceholder.typicode.com/users"
        response = request.urlopen(url)
        data = json.loads(response.read().decode())

        for user_data in data:
            geo_data = user_data['address']['geo']
            geo = Geo.objects.create(**geo_data)

            address_data = user_data['address']
            address_data['geo'] = geo
            address = Address.objects.create(**address_data)

            company_data = user_data['company']
            company = Company.objects.create(**company_data)

            user_data['address'] = address
            user_data['company'] = company

            Profile.objects.create(**user_data)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
