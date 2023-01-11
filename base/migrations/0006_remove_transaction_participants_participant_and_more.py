# Generated by Django 4.1.5 on 2023-01-06 06:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_transaction_owner_alter_transaction_paidby"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="participants",
        ),
        migrations.CreateModel(
            name="Participant",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "createdAt",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                (
                    "amountOwes",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "participant",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="base.profile"
                    ),
                ),
                (
                    "transaction",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.transaction",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="transaction",
            name="participants",
            field=models.ManyToManyField(
                related_name="participants", to="base.participant"
            ),
        ),
    ]