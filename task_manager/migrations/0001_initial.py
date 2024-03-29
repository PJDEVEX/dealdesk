# Generated by Django 3.2.19 on 2023-07-10 14:59

from django.db import migrations, models
import task_manager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskManager', fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('title', models.CharField(
                        max_length=55)), ('description', models.CharField(
                            max_length=255)), ('due_date', models.DateField()), ('status', models.CharField(
                                choices=[
                                    ('TBD', 'To Do'), ('D', 'Done')], default='To Do', max_length=50)), ('priority', models.CharField(
                                        choices=[
                                            ('N', 'Normal'), ('U', 'Urgent')], default='Normal', max_length=50)), ('assigned_to', models.ForeignKey(
                                                on_delete=models.SET(
                                                    task_manager.models.get_salesman), related_name='tasks', to='team.sar')), ], options={
                'ordering': ['due_date'], }, ), ]
