from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    zip_zode = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)

