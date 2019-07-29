from django.db import models

# Create your models here.
class main(models.Model):
    category = models.CharField(max_length = 20)
    title = models.CharField(max_length = 20)
    contact = models.IntegerField()
    address = models.CharField(max_length = 30)

class to_approve(models.Model):
    category = models.CharField(max_length = 20)
    title = models.CharField(max_length = 20)
    address = models.CharField(max_length = 30)
    contact = models.IntegerField()

