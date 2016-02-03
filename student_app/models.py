from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class student (models.Model):
	name = models.CharField(max_length=30)
	sex = models.CharField(max_length=30)
	age =  models.IntegerField()
	mark = models.IntegerField()
	
	

class UserProfile(models.Model):

	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)
    
    


 