from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from task_manager.models import TaskManager
from client.models import Client
from project.models import Project


# Create your models here.


class Manager(models.Model):
    mng_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    salesman = models.CharField(max_length=55)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Team.Manager'
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sar(models.Model):
    sar_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Team.Sar'
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
