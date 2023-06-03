# Generated by Django 3.2.19 on 2023-06-02 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='forecast_pxp',
        ),
        migrations.AlterField(
            model_name='project',
            name='winning_chance',
            field=models.DecimalField(choices=[(0.0, '0% - No Chance'), (0.2, '20% - Very Low, 20%'), (0.5, '50% - May be'), (0.75, '75% - Highly Likely'), (0.9, '90% - WON PENDING PO'), (1.0, '100% - WON with PO')], decimal_places=2, max_digits=3),
        ),
    ]