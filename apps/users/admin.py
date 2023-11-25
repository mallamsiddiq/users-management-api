from django.contrib import admin
from .models import Geo, Address, Company, Profile

[admin.site.register(obj) for obj in \
 (Geo, Address, Company, Profile)]


# Register your models here.
