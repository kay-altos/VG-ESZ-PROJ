from django.db import models
# Create your models here.
class SitePropertis(models.Model):
    property_name = models.CharField(max_length=60)
    property_data = models.TextField(max_length=5000)
