# Generated by Django 3.2.4 on 2021-12-25 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20211225_0038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
    ]
