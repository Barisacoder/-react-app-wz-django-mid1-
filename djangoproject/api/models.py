from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=150)
    grade =  models.TextField()

    def __str__(self):
        return self.name