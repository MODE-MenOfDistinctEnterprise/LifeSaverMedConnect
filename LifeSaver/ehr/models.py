from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField()

    def __str__(self):
        return self.name