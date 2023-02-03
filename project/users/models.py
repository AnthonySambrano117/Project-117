from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class BaseModel(models.Model):
    username = models.CharField(validators=[MinLengthValidator(11)], max_length=32)
    password = models.CharField(validators=[MinLengthValidator(11)], max_length=32)


# Create a form class that inherits from BaseForm
class RegistrationModel(BaseModel):
    email = models.EmailField()
    password_confirmation = models.CharField(validators=[MinLengthValidator(11)], max_length=32)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


def __str__(self):
    return self.username



