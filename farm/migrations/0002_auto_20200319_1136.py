# Generated by Django 3.0.3 on 2020-03-19 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='farm',
            options={'ordering': ['-total_land_available']},
        ),
    ]