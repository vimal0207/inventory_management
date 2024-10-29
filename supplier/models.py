from django.db import models

from base.models import BaseModel

class Supplier(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    contact_info = models.TextField(blank=True)

    def __str__(self):
        return self.name
