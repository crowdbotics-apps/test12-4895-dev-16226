# Generated by Django 2.2.17 on 2020-12-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20201203_1126"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="test",
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
