from tokenize import Name
from django.db import models
from django.forms import CharField
from sqlalchemy import null, true

# Create your models here.
class Product(models.Model):
    Name = CharField(max_length=200)