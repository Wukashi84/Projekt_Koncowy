# Generated by Django 4.2.9 on 2024-02-29 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("FleetManagement", "0013_uzytkownik_remove_pojazd_mpk_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="uzytkownik",
            name="pojazd",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="FleetManagement.pojazd",
            ),
        ),
    ]
