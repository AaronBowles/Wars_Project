# Generated by Django 2.2.7 on 2019-11-07 21:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wars', '0004_auto_20191107_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='key_technologies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), size=None),
        ),
    ]