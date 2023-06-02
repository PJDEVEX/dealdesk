from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.

PROJECT_STATUS = [
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
            (0.00, "0% - No Chance"),
            (0.20, "20% - Very Low, 20%"),
            (0.50, "50% - May be"),
            (0.75, "75% - Highly Likely"),
            (0.90, "90% - WON PENDING PO"),
            (1.00, "100% - WON with PO"),
        ]


class Brand(models.Model):
    """
    Represents a brand model.

    This class defines the Brand model, which represents a brand
    in the system. It has fields to store the brand ID,
    brand name, and timestamps for creation and updates.

    Attributes:
        brand (str): The name or description of the brand.
        created_on (DateTimeField): timestamp of when brand was created.
        updated_on (DateTimeField): timestamp of last update to the brand.
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

    This class defines the Category model, which is used to categorize
    various items or entities in the system. It has fields to store
    the category ID, category name, and timestamps for creation and
    updates.

    Attributes:
        category (str): The name or description of the category.
        created_on (DateTimeField): timestamp when the category was created.
        updated_on (DateTimeField): timestamp of last update to the category.
    """
    category = models.CharField(max_length=55, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category']
        verbose_name_plural = "categories"  # Add pural verbose for the model

    def __str__(self):
        return self.category


class Project(models.Model):
    name = models.CharField(max_length=100, null=False)
    client = models.ForeignKey(
        'client.Client',
        on_delete=models.CASCADE,
        related_name='projects'
    )
    location = models.CharField(max_length=55, null=False)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    salesman = models.ForeignKey(
        'team.Sar',
        on_delete=models.CASCADE,
        related_name='projects',
    )
    manager = models.ForeignKey(
        'team.Manager',
        on_delete=models.CASCADE,
        related_name='projects'
    )
    type_of_construction = models.CharField(
        max_length=20,
        choices=TYPE_OF_CONSTRUCTION,
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    project_status = models.TextField(
        max_length=55,
        choices=PROJECT_STATUS,
        null=False,
        default="Active"
    )
    est_closing_date = models.DateField(null=False)
    est_date_of_delivery = models.DateField()
    potential_value = models.FloatField(null=False)
    winning_chance = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        choices=WINNING_CHANCE,
        null=False
    )

    def save(self, *args, **kwargs):
        """
        Save the project instance.

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
