# Generated by Django 4.1.2 on 2023-08-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_alter_cards_card_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cards", name="card_id", field=models.IntegerField(),
        ),
    ]
