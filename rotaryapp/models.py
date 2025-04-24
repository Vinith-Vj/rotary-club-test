from django.db import models

# Create your models here.

class homeCoverImage(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class History(models.Model):
    president_name = models.CharField(max_length=400, blank=False)
    president_image=models.ImageField(upload_to='images/',blank=False,null=True)
    secretary_name = models.CharField(max_length=400, blank=False)
    secretary_image=models.ImageField(upload_to='images/',blank=False,null=True)
    start_year = models.IntegerField(blank=False)
    end_year = models.IntegerField(blank=False)

    def __str__(self):
        return f"President---Secretary({self.start_year} - {self.end_year})"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Membership(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    profession = models.CharField(max_length=100, blank=True)
    age = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=15)
    secondary_number = models.CharField(max_length=15, blank=True)
    phone_type = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
from django.db import models

class Sponsor(models.Model):
    organization_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.organization_name} - {self.contact_name}"

from django.db import models

class Uyare(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    qualification = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return f"{self.title} - {self.date}"