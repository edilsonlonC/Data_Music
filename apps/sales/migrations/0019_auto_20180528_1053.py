# Generated by Django 2.0.4 on 2018-05-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0018_auto_20180528_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='Price_sale',
            field=models.FloatField(default=0),
        ),
    ]