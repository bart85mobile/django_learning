from django.db import models
import uuid

from django.db.models.deletion import CASCADE

class BusinessEntity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    company_name = models.CharField(max_length=200)
    company_type = models.CharField(max_length=10)
    address = models.CharField(max_length=2000)
    address2 = models.CharField(max_length=2000)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name