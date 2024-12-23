# Generated by Django 4.2.1 on 2023-05-26 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_form_gender_alter_form_interest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_idea', models.CharField(max_length=300)),
                ('date_time', models.TimeField()),
                ('date_location', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('PND', 'PENDING'), ('ACC', 'ACCEPTED'), ('DEC', 'DECLINED')], default='PND', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('receiverId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiverId', to='application.user')),
                ('senderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senderId', to='application.user')),
            ],
        ),
    ]
