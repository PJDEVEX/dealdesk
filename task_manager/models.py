from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.

STATUS_CHOICES = [
    ("TBD", "To Do"),
    ("D", "Done"),
]

PRIORITY_CHOICES = [
    ("N", "Normal"),
    ("U", "Urgent"),
]


class TaskManager(models.Model):
    title = models.CharField(max_length=55, null=False)
    description = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=False)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="To Do",
        null=False
        )
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY_CHOICES,
        default="Normal",
        null=False)
    assigned_to = models.ForeignKey(
        'team.Sar',
        on_delete=models.CASCADE,
        related_name='tasks')

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title
