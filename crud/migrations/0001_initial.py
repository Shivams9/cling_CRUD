# Generated by Django 4.1.4 on 2023-04-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crudModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_address', models.CharField(max_length=100)),
                ('user_mobilenumber', models.CharField(max_length=10)),
            ],
        ),
    ]