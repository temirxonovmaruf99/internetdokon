from django.db import models
from account.models import User
from internetdokon.validators import PhoneValidator
from main.models import Product


class Order(models.Model):
    STATUS_YES = 1
    STATUS_NO = 0

    PAYMENT_STATUS_NEW = 0
    PAYMENT_STATUS_PREPARE = 1
    PAYMENT_STATUS_COMPLETE = 2

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    address = models.TextField()
    phone = models.CharField(max_length=16, validators=[PhoneValidator()])
    zip_code = models.CharField(max_length=20)
    status = models.SmallIntegerField(choices=(
        (STATUS_YES, "Bor"),
        (STATUS_NO, "Yo'q")
    ))

    payment_status = models.SmallIntegerField(choices=(
        (PAYMENT_STATUS_NEW, "New"),
        (PAYMENT_STATUS_PREPARE, "Prepare"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
    ), default=PAYMENT_STATUS_NEW)
    order_at = models.DateTimeField(auto_now_add=True)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    amount = models.IntegerField()


