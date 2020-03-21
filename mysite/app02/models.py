from django.db import models

# Create your models here.
class Store(models.Model):
    proxy = models.CharField(max_length=20)


class SuccessStore(models.Model):
    proxy = models.CharField(max_length=20)


class FailStore(models.Model):
    proxy = models.CharField(max_length=20)