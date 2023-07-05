from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from decimal import Decimal


#  Get a default ID
def get_manager():
    return 2


def get_salesman():
    return 2


def get_client():
    return 3


def get_brand():
    return 2


def get_category():
    return 2


LEAD_STATUS = [
            ("Atv", "Active"),
            ("O/h", "On hold"),
            ("P.won", "Partially won"),
            ("Won", "Won")
        ]

TYPE_OF_CONSTRUCTION = [
            ("NC", "New Construction"),
            ("RF", "Refurbishment")
        ]

WINNING_CHANCE = [
    (Decimal('0.00'), "0% - No Chance"),
    (Decimal('0.20'), "20% - Very Low, 20%"),
    (Decimal('0.50'), "50% - May be"),
    (Decimal('0.75'), "75% - Highly Likely"),
    (Decimal('0.90'), "90% - WON PENDING PO"),
    (Decimal('1.00'), "100% - WON with PO"),
    ]


class Brand(models.Model):
    """
    Represents a brand model.
    """
    brand = models.CharField(max_length=55, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['brand']
    
    def __str__(self):
        return self.brand


class Category(models.Model):
    """
    Represents a category model.
    """
    category = models.CharField(max_length=55, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category


class LeadMaster(models.Model):
    name = models.CharField(max_length=100, null=False)
    client = models.ForeignKey(
        'client.Client',
        on_delete=models.SET(get_client),
        related_name='lead_masters'
    )
    location = models.CharField(max_length=55, null=False)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET(get_brand),
        related_name='lead_masters'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    salesman = models.ForeignKey(
        'team.Sar',
        on_delete=models.SET(get_salesman),
        related_name='lead_masters',
    )
    manager = models.ForeignKey(
        'team.Manager',
        on_delete=models.SET(get_manager),
        related_name='lead_masters'
    )
    type_of_construction = models.CharField(
        max_length=20,
        choices=TYPE_OF_CONSTRUCTION,
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET(get_category),
        related_name='lead_masters'
    )
    lead_status = models.TextField(
        max_length=55,
        choices=LEAD_STATUS,
        null=False,
        default="Active"
    )
    est_closing_date = models.DateField(null=False)
    est_date_of_delivery = models.DateField()
    potential_value = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        null=False)
    winning_chance = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        choices=WINNING_CHANCE,
        null=False
    )
    forecast_pxp = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        """
        Save the lead_master instance.

        This method overrides the default save method to calculate
        the forecasted potential value (forecast_pxp) based on the
        potential value and winning chance before saving the instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        self.forecast_pxp = self.potential_value * self.winning_chance
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
