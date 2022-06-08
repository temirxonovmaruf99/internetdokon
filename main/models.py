from django.db import models
from account.models import User
from common.models import Country, Region, District
from internetdokon.validators import PhoneValidator


class Carusel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    content = models.TextField()


class Product(models.Model):
    STATUS_YES = 1
    STATUS_NO = 0
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField()
    available = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    status = models.SmallIntegerField(choices=(
        (STATUS_YES, "Bor"),
        (STATUS_NO, "Qolmagan")
    ))

    def __str__(self):
        return self.name

    class Meta:
        indexes = (
            models.Index(fields=('status',)),
        )







