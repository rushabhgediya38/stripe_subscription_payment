# Generated by Django 3.2 on 2021-04-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptionsApp', '0002_auto_20210413_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripecustomer',
            name='is_free',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
