from django.db import models

# Create your models here.
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=20)
    age = models.IntegerField()
    bloodGroup = models.CharField(max_length=5)
    rollNumber = models.CharField(max_length=15)
    currMeds = models.TextField()


