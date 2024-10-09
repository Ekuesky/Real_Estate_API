# Generated by Django 5.0.9 on 2024-10-08 19:08

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("apartments", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Issue",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=255, verbose_name="Issue Title")),
                ("description", models.TextField(verbose_name="Issue Description")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("reported", "Reported"),
                            ("resolved", "Resolved"),
                            ("in_progress", "In Progress"),
                        ],
                        default="reported",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("low", "Low"),
                            ("medium", "Medium"),
                            ("high", "High"),
                        ],
                        default="low",
                        max_length=20,
                        verbose_name="Priority",
                    ),
                ),
                (
                    "resolved_on",
                    models.DateField(blank=True, null=True, verbose_name="Resolved On"),
                ),
                (
                    "apartment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="issues",
                        to="apartments.apartment",
                        verbose_name="Apartment",
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="assigned_to_issues",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Assigned to",
                    ),
                ),
                (
                    "reported_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reported_by_issues",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Reported by",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
    ]
