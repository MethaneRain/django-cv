from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.TextField()#models.CharField()
    description = models.TextField()
    price = models.TextField()#models.DecimalField()
    summary = models.TextField(default="Write a summary")