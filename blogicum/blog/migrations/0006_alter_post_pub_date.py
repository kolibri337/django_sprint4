# Generated by Django 3.2.16 on 2023-06-02 20:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0005_auto_20230602_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 2, 20, 15, 31, 109943, tzinfo=utc
                ),
                help_text='Если установить дату и время в будущем — можно делать отложенные публикации.',
                verbose_name='Дата и время публикации',
            ),
        ),
    ]
