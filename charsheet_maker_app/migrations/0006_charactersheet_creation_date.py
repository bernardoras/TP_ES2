# Generated by Django 5.1.3 on 2024-11-27 14:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charsheet_maker_app', '0005_charactersheet_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactersheet',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date was created'),
        ),
    ]