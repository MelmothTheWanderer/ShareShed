# Generated by Django 4.2.9 on 2024-02-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_alt_text',
            field=models.CharField(default='alt', max_length=200),
            preserve_default=False,
        ),
    ]
