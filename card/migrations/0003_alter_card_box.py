# Generated by Django 4.2.4 on 2023-11-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("card", "0002_alter_card_box"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="box",
            field=models.IntegerField(
                choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1
            ),
        ),
    ]
