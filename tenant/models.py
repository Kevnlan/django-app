from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True, null=True)
    next_of_kin = models.CharField(max_length=200, blank=True, null=True)
    is_tenant = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.name    


    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()


class Building(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buildingsowner")
    tenant = models.OneToOneField(User, on_delete=models.CASCADE, related_name="tenants", blank=True, null=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    units_count = models.IntegerField()

    def __str__(self):
        return self.name

class BuildingTenant(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="building") 
    tenant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buildingtenants")
    checkInDate = models.DateTimeField()
    contractAmount = models.FloatField()
    status = models.BooleanField(default=True)