from django.db import models
from service.django_ext.models import BaseModel


class User(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'

