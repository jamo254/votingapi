# Generated by Django 2.2.10 on 2021-10-23 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='start_date',
            field=models.DateTimeField(blank=True, verbose_name='date published'),
        ),
    ]
