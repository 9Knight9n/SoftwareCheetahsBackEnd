# Generated by Django 3.1.7 on 2021-03-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(blank=True, max_length=20)),
                ('role', models.CharField(default='normal-user', max_length=20, verbose_name='role')),
                ('national_code', models.IntegerField(blank=True, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birthday', models.DateField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='users/images/')),
                ('bio', models.TextField(blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
