# Generated by Django 4.2.17 on 2024-12-23 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Journey",
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
                ("PID", models.IntegerField(null=True)),
                ("fullname", models.CharField(max_length=255)),
                ("start", models.CharField(max_length=255)),
                ("end", models.CharField(max_length=255)),
                ("start_time", models.TimeField(null=True)),
            ],
        ),
    ]