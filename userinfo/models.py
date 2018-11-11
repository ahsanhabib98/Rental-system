from django.db import models
from django.contrib.auth.models import User

class Division(models.Model):
    division_name = models.CharField(max_length=50)
    def __str__(self):
        return self.division_name

class District(models.Model):
    district_name = models.CharField(max_length=50)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    def __str__(self):
        return self.district_name

class Area(models.Model):
    area_name = models.CharField(max_length=50)
    District = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
        return self.area_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    profile_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    nid = models.IntegerField()
    is_owner = models.BooleanField(default=False)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    phone = models.IntegerField()
    def __str__(self):
        return self.profile_name

# Create your models here.
