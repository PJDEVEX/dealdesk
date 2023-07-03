from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from team.models import Sar, Manager

# Create your models here.

CLIENT_TYPE_CHOICES = [
        ("ARC", "Architect"),
        ("PLM", "Plumbing Contractor"),
        ("DVP", "Developer"),
        ("EPC", "EPC Contractor"),
        ("CLN", "End-Client"),
        ]


class Client(models.Model):
    company_name = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=55, null=False)
    last_name = models.CharField(max_length=55, null=False)
    client_type = models.CharField(
        max_length=55,
        choices=CLIENT_TYPE_CHOICES,
        null=False,
        default="CLN"
    )
    address1 = models.CharField(max_length=255, null=False)
    address2 = models.CharField(max_length=255, null=False)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    salesman = models.ForeignKey(
        Sar,
        on_delete=models.CASCADE,
        null=True,  # Set the foreign key field as nullable
        blank=False,  # Doesn't allow the foreign key field to be empty in forms,
        related_name='clients'
    )
    manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='clients'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        db_table = 'Client.Client'
        ordering = ['company_name']

    def __str__(self):
        return self.company_name
