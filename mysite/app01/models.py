from django.db import models


class Store(models.Model):
    proxy = models.CharField(max_length=20)


class SuccessStore(models.Model):
    proxy = models.CharField(max_length=20)


class FailStore(models.Model):
    proxy = models.CharField(max_length=20)