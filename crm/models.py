from django.db import models

# Create your models here.
#Employee [name,email,phone,salary,department,location]

class Employee(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    salary = models.DecimalField(max_digits=10,decimal_places=2)

    department = models.CharField(max_length=200)

    location = models.CharField(max_length=200)


