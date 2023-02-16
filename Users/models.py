from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.
def is_mail_esprit(mail):
    if str(mail).endswith('@esprit.tn')==False:
        raise ValidationError('Please check your mail !!!')
class Person(AbstractUser):
    cin=models.CharField("CIN",primary_key=True ,max_length=8 ,validators=[MaxLengthValidator(8),MinLengthValidator(8)])
    email=models.EmailField(unique=True,validators=[is_mail_esprit])

