# Generated by Django 2.0.4 on 2018-05-24 06:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_remove_sale_date_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='Date_sale',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
