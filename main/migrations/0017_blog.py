# Generated by Django 4.1.2 on 2023-09-25 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0016_appointments_usern"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("blog_name", models.CharField(max_length=254)),
                ("blog_content", models.TextField()),
                ("blog_author", models.CharField(max_length=254)),
                ("uname", models.CharField(max_length=250)),
            ],
        ),
    ]
