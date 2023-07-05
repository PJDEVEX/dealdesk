from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


#  Get a default ID
def get_manager():
    return 2


class Manager(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Team.Manager'
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sar(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    manager = models.ForeignKey(
        Manager,
        on_delete=models.SET(get_manager),
        related_name='sars',)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Team.Sar'
        ordering = ['first_name']
        verbose_name_plural = 'Sars'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
