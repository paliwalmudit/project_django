# Generated by Django 4.1.2 on 2023-08-02 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_cards_card_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="cards",
            name="card_details",
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name="cards", name="card_description", field=models.TextField(),
        ),
    ]