from django.db import models

# Create your models here.

class Contact(models.Model):
	#c_id = models.AutoField()
	first_name =   models.CharField(max_length=100,blank=False)
	second_name = models.CharField(max_length=100,blank=False)
	email = models.EmailField(max_length=70, null=True, blank=True, unique=False)