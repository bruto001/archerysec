# Generated by Django 3.2.15 on 2022-08-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0016_auto_20220824_0432"),
    ]

    operations = [
        migrations.AlterField(
            model_name="monthdb",
            name="critical",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]