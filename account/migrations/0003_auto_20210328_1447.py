# Generated by Django 3.1.7 on 2021-03-28 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210328_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
