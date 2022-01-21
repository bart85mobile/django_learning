from django.db import models
import uuid

from django.db.models.deletion import CASCADE

class ExternalEntity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    address2 = models.CharField(max_length=2000, null=True, blank=True)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=200, null=True, blank=True)
    postcode = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
    
    class Meta:
        ordering = ['-created_at']
        
class InternalEntity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    address2 = models.CharField(max_length=2000, null=True, blank=True)
    city = models.CharField(max_length=200)
    region = models.CharField(max_length=200, null=True, blank=True)
    postcode = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
    
    class Meta:
        ordering = ['-created_at']
        
class Contract(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    contract_name = models.CharField(max_length=200)
    external_entity = models.ForeignKey(ExternalEntity, on_delete=models.CASCADE)
    internal_entity = models.ForeignKey(InternalEntity, on_delete=models.CASCADE)
    contract_date = models.DateField(default='1900-01-01')
    contract_extension = models.CharField(max_length=4, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = [['external_entity', 'internal_entity', 'contract_date', 'contract_extension']]

    def __str__(self):
        return self.contract_name
