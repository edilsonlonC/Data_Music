# Generated by Django 2.0.4 on 2018-05-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='Id_Instrumets',
        ),
        migrations.AddField(
            model_name='sale',
            name='Id_Instrumets',
            field=models.ManyToManyField(to='instruments.Instruments'),
        ),
    ]