# Generated by Django 4.1.2 on 2023-08-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_cards_card_details"),
    ]

    operations = [
        migrations.AddField(
            model_name="cards", name="card_id", field=models.IntegerField(default=None),
        ),
    ]
