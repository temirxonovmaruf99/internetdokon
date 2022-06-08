from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100)
