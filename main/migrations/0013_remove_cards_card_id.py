# Generated by Django 4.1.2 on 2023-08-03 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_cards_card_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="cards", name="card_id",),
    ]
