# Generated by Django 2.0.4 on 2018-05-01 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20180501_2206'),
        ('instruments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruments',
            name='id_Sale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.Sale'),
        ),
    ]
