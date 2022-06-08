from django.core.exceptions import ValidationError
import re

from django.utils.deconstruct import deconstructible
import phonenumbers


@deconstructible
class PhoneValidator:
    requires_context = False

    @staticmethod
    def clean(value):
        return re.sub('[^0-9]+', '', value)

    @staticmethod
    def validate(value):
        try:
            z = phonenumbers.parse("+" + value)
            if not phonenumbers.is_valid_number(z):
                return False
        except:
            return False

        if len(value) != 12 or not value.startswith("998"):
            return False

        return True

    @staticmethod
    def format(value):
        try:
            z = phonenumbers.parse("+" + value)
            if not phonenumbers.is_valid_number(z):
                return value

            return phonenumbers.format_number(z, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        except:
            return value


    def __call__(self, value):
        if not PhoneValidator.validate(value):
            raise ValidationError("Kirtilgan qiymat telefon raqam emas")





