# Generated by Django 3.1.7 on 2021-03-28 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210328_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='national_code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
