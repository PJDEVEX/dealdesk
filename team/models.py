from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


def get_manager():
    """
    Get the default ID for the manager.
    """
    return 2


class Manager(models.Model):
    """
    Represents a manager model.
    """
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta options for the Manager model.
        """
        db_table = 'Team.Manager'
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name}"


class Sar(models.Model):
    """
    Represents a SAR (Sales Account Representative) model.
    """
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    manager = models.ForeignKey(
        Manager,
        on_delete=models.SET(get_manager),
        related_name='sars',
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta options for the Sar model.
        """
        db_table = 'Team.Sar'
        ordering = ['first_name']
        verbose_name_plural = 'Sars'

    def __str__(self):
        return f"{self.first_name}"
