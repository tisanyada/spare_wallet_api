# Generated by Django 4.1.3 on 2023-01-11 08:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DebitCard",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("card_name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "card_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("card_type", models.CharField(blank=True, max_length=255, null=True)),
                ("card_expiration", models.DateField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Wallet",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "wallet_number",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "wallet_balance",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="SpareCard",
        ),
    ]
