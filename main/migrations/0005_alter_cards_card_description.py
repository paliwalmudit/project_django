# Generated by Django 4.1.2 on 2023-08-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_remove_cards_card_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cards",
            name="card_description",
            field=models.CharField(max_length=1000),
        ),
    ]
