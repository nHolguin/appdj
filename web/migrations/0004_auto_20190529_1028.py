# Generated by Django 2.2.1 on 2019-05-29 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190529_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='inicio',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 29, 14, 28, 9, 960339, tzinfo=utc)),
        ),
    ]
