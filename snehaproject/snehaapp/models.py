from django.db import models

# Create your models here.
class web1(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    img = models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    desc=models.TextField()

    def __str__(self):
        return self.name