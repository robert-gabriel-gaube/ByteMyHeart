# Generated by Django 4.2.1 on 2023-05-24 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='receiverID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user'),
        ),
    ]