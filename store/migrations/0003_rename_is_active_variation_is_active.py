# Generated by Django 4.2.8 on 2024-02-29 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_variation"),
    ]

    operations = [
        migrations.RenameField(
            model_name="variation",
            old_name="is_Active",
            new_name="is_active",
        ),
    ]
