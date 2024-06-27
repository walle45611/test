from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    town = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name