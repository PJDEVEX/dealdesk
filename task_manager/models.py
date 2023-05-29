from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.


class TaskManager(models.Model):
    task_id = models.CharField(
        max_length=10,
        primary_key=True
        )
    title = models.CharField(max_length=55, null=False)
    description = models.TextField(100)
    due_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ("TBD", "To-be-Done"),
            ("D", "Done")
        ],
        null=False
        )
    priority = models.CharField(
        max_length=50,
        choices=[
            ("N", "Normal"),
            ("U", "Urgent")
        ],
        default="Normal",
        null=False)
    assigned_to = models.ForeignKey(
        'team.SAR',
        on_delete=models.CASCADE,
        related_name='sar_tasks')

    class Meta:
        ordering = ['due_date']

    def __str__(self):
        return self.title
