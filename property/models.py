from django.db import models
from userinfo.models import Profile

# Create your models here.


class AddProperty(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='property_image', blank=True)
	detail = models.TextField()
	daily = models.BooleanField(blank=False)
	weekly = models.BooleanField(blank=False)
	monthly = models.BooleanField(blank=False)
	is_available = models.BooleanField(blank=False)

	def __str__(self):
		return self.name
