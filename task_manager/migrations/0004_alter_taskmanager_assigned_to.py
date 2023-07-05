# Generated by Django 3.2.19 on 2023-07-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_alter_sar_manager'),
        ('task_manager', '0003_alter_taskmanager_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmanager',
            name='assigned_to',
            field=models.ForeignKey(on_delete=models.SET('Salesman to be allocated'), related_name='tasks', to='team.sar'),
        ),
    ]
