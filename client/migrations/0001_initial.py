# Generated by Django 3.2.19 on 2023-07-10 14:59

import client.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('client_type', models.CharField(choices=[('ARC', 'Architect'), ('PLM', 'Plumbing Contractor'), ('DVP', 'Developer'), ('EPC', 'EPC Contractor'), ('CLN', 'End-Client')], default='CLN', max_length=55)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(on_delete=models.SET(client.models.get_manager), related_name='clients', to='team.manager')),
                ('salesman', models.ForeignKey(on_delete=models.SET(client.models.get_salesman), related_name='clients', to='team.sar')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'Client.Client',
                'ordering': ['company_name'],
            },
        ),
    ]
