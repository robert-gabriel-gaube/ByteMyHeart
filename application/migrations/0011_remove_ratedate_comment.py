# Generated by Django 4.2.1 on 2023-11-05 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_ratedate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratedate',
            name='comment',
        ),
    ]
