from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='student/', blank=True, null=True)

    def __str__(self):
        return self.name
