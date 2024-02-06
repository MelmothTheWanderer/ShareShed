# Generated by Django 4.2.9 on 2024-02-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=200, unique=True)),
                ('in_stock', models.BooleanField(default=True)),
            ],
        ),
    ]
