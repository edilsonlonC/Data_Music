# Generated by Django 2.0.4 on 2018-05-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20180522_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='Description',
        ),
        migrations.AddField(
            model_name='sale',
            name='Price_sale',
            field=models.FloatField(default=0),
        ),
    ]
