# Generated by Django 5.0.6 on 2024-05-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobilenumber', models.IntegerField()),
                ('emailaddress', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=120)),
            ],
        ),
    ]
