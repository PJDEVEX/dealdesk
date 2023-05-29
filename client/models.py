from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Client(models.Model):
    client_id = models.CharField(max_length=10, primary_key=True)
    client_company = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=55, null=False)
    last_name = models.CharField(max_length=55, null=False)
    CLIENT_TYPE_CHOICES = [
        ("ARC", "Architect"),
        ("PLM", "Plumbing Contractor"),
        ("DVP", "Developer"),
        ("EPC", "EPC Contractor"),
        ("CLN", "End-Client"),
    ]
    client_type = models.CharField(
        max_length=55,
        choices=CLIENT_TYPE_CHOICES,
        null=False,
        default="CLN"
    )
    address1 = models.CharField(max_length=55, null=False)
    address2 = models.CharField(max_length=55, null=False)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=200, null=False)
    country = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    salesman = models.ForeignKey(
        'team.Sar',
        on_delete=models.SET_NULL,
        null=True,
        related_name='Sar_clients'
    )
    manager = models.ForeignKey(
        'team.Manager',
        on_delete=models.SET_NULL,
        null=True,
        related_name='Manager_clients'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Client.Client'
        ordering = ['client_company']

    def __str__(self):
        return self.client_company
