# Generated by Django 2.2.10 on 2021-10-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apicore', '0005_auto_20211025_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(verbose_name='end date'),
        ),
    ]
