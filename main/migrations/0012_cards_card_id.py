# Generated by Django 4.1.2 on 2023-08-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_remove_cards_card_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="cards",
            name="card_id",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
