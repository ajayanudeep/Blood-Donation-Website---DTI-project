from django.db import models

# Create your models here.


class details(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, default="male")
    blood_type = models.CharField(max_length=3)
    mobile = models.BigIntegerField()
    hospital = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
