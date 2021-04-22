from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Building, BuildingTenant

admin.site.register(Profile)
admin.site.register(Building)
admin.site.register(BuildingTenant)