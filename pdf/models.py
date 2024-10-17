from django.db import models

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True,null=False, blank=False,default=None)
    email = models.EmailField(max_length=254, unique=True,default=None)
    phone = models.IntegerField(unique=True, default=None)
    address = models.TextField(max_length=200,default=None)
    city = models.CharField(max_length=100, default=None)
    country = models.CharField(max_length=100, default=None)
    summary = models.TextField(max_length=2000,default=None)
    degree = models.CharField(max_length=100, default=None)
    school = models.CharField(max_length=100,default=None)
    university = models.CharField(max_length=100,default=None)
    previous_work = models.TextField(max_length=2000,default=None)   
    skills = models.TextField(max_length=2000,default=None)

    REQUIRED_FIELDS = [name,phone,email]

    def __str__(self):
        return self.name
