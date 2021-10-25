# Generated by Django 2.2.10 on 2021-10-25 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apicore', '0004_question_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]