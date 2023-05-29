from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Brand(models.Model):
    """
    Represents a brand model.

    This class defines the Brand model, which represents a brand
    in the system. It has fields to store the brand ID,
    brand name, and timestamps for creation and updates.

    Attributes:
        brand_id (str): The unique identifier of the brand.
        brand (str): The name or description of the brand.
        created_on (DateTimeField): timestamp of when brand was created.
        updated_on (DateTimeField): timestamp of last update to the brand.
    """
    brand_id = models.CharField(max_length=10, unique=True)
    brand = models.TextField(max_length=55, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['brand']


class Category(models.Model):
    """
    Represents a category model.

    This class defines the Category model, which is used to categorize
    various items or entities in the system. It has fields to store
    the category ID, category name, and timestamps for creation and
    updates.

    Attributes:
        category_id (str): The unique identifier of the category.
        category (str): The name or description of the category.
        created_on (DateTimeField): timestamp when the category was created.
        updated_on (DateTimeField): timestamp of last update to the category.
    """
    category_id = models.CharField(max_length=10, unique=True)
    category = models.TextField(max_length=55, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category']


class Project(models.Model):
    project_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, null=False)
    client = models.ForeignKey(
        'client.Client',
        on_delete=models.CASCADE,
        related_name='client_projects'
    )
    location = models.CharField(max_length=55, null=False)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='brand_projects'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    salesman = models.ForeignKey(
        'team.Sar',
        on_delete=models.CASCADE,
        related_name='salesman_projects'
    )
    manager = models.ForeignKey(
        'team.Manager',
        on_delete=models.CASCADE,
        related_name='manager_projects'
    )
    type_of_construction = models.CharField(
        max_length=20,
        choices=[
            ("NC", "New Construction"),
            ("RF", "Refurbishment")
        ],
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category_projects'
    )
    project_status = models.TextField(
        max_length=55,
        choices=[
            ("Atv", "Active"),
            ("O/h", "On hold"),
            ("P.won", "Partially won"),
            ("Won", "Won")
        ],
        null=False,
        default="Active"
    )
    est_closing_date = models.DateField(null=False)
    est_date_of_delivery = models.DateField()
    potential_value = models.FloatField(null=False)
    winning_chance = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        choices=[
            (0.00, "No Chance"),
            (0.20, "Very Low"),
            (0.50, "May be"),
            (0.75, "Highly Likely"),
            (0.90, "WON PENDING PO"),
            (1.00, "WON with PO"),
        ],
        null=False
    )
    forecast_pxp = models.FloatField()

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
        ordering = ['-created_on']

    def __str__(self):
        return self.name
