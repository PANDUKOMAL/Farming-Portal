# Generated by Django 3.0.4 on 2020-06-18 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20200616_1122'),
        ('checkout', '0007_remove_addressandpayment_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressandpayment',
            name='id',
        ),
        migrations.AddField(
            model_name='addressandpayment',
            name='order_id',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cart.Order'),
            preserve_default=False,
        ),
    ]