from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True, unique=True)
	email = models.CharField(max_length=200, null=True, unique=True)
	profile_pic = models.ImageField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Contact(models.Model):
    name = models.CharField(max_length=124)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    message = models.TextField()

    def __str__(self):
        return self.name