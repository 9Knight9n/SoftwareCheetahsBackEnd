# Generated by Django 3.1.7 on 2021-03-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210328_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
