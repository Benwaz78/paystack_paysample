# Generated by Django 3.0.5 on 2020-06-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_starter_app', '0002_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
