# Generated by Django 5.1.2 on 2024-10-29 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_stockchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='alert_threshold',
            field=models.PositiveIntegerField(default=5),
        ),
    ]
