# Generated by Django 4.2.8 on 2024-03-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
    ]
