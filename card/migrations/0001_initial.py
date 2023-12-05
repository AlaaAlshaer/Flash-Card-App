# Generated by Django 4.2.4 on 2023-11-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
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
                ("question", models.CharField(max_length=100)),
                ("answer", models.CharField(max_length=100)),
                (
                    "box",
                    models.IntegerField(
                        choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]