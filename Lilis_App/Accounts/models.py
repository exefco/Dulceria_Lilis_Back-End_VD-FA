from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    STATUS_CHOICES = [("ACTIVE", "Active"), 
                      ("INACTIVE", "Inactive")]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default="ACTIVE")
    created_at = models.DateTimeField(auto_add_now=True, help_text="Fecha/hora de creación")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha/hora de la última actualización")
    deleted_at = models.DateTimeField(null=True, help_text="Marca de borrado lógico.",blank=True)
    class Meta:
        abstract = True


   