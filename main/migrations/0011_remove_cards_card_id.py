# Generated by Django 4.1.2 on 2023-08-03 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_alter_cards_card_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="cards", name="card_id",),
    ]
