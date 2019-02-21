from django.db import models
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    #c_id = models.AutoField()
    first_name =   models.CharField(max_length=100,blank=False)
    second_name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=False)


    def __str__(self):
        return "{} - {} - {}".format(self.id,self.first_name, self.second_name,)

    def get_absolute_url(self):
        return reverse('contact_datails', args=[str(self.id)])
    