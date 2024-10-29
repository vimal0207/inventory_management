# Generated by Django 5.1.2 on 2024-10-28 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
