# Generated by Django 5.1.7 on 2025-06-09 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DHCPConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subnet", models.GenericIPAddressField()),
                ("min_ip_pool", models.GenericIPAddressField()),
                ("max_ip_pool", models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("file", models.FileField(null=True, upload_to="conf/")),
            ],
        ),
        migrations.CreateModel(
            name="Device",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("serial_number", models.CharField(max_length=255, unique=True)),
                ("ip", models.GenericIPAddressField(unique=True)),
                ("hostname", models.CharField(blank=True, max_length=255, null=True)),
                ("configured", models.BooleanField(default=False)),
                (
                    "subnet_mask",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "default_gateway",
                    models.GenericIPAddressField(blank=True, null=True),
                ),
                ("login", models.CharField(blank=True, max_length=255, null=True)),
                ("password", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "template",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="devices",
                        to="device.template",
                    ),
                ),
            ],
        ),
    ]
