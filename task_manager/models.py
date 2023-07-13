from django.db import models
from django.contrib.auth.models import User


def get_salesman():
    """
    Get the default ID for the salesman.
    """
    return 2


STATUS_CHOICES = [
    ("TBD", "To Do"),
    ("D", "Done"),
]

PRIORITY_CHOICES = [
    ("N", "Normal"),
    ("U", "Urgent"),
]


class TaskManager(models.Model):
    """
    Represents a task manager model.
    """
    title = models.CharField(max_length=55, null=False)
    description = models.CharField(max_length=255)
    due_date = models.DateField(null=False)
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
        null=False
    )
    assigned_to = models.ForeignKey(
        'team.Sar',
        on_delete=models.SET(get_salesman),
        related_name='tasks'
    )

    class Meta:
        """
        Meta options for the TaskManager model.
        """
        ordering = ['due_date']

    def __str__(self):
        return self.title
