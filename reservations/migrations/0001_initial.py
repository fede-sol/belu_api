# Generated by Django 5.1.2 on 2024-10-13 03:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('belu_auth', '0001_initial'),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.room')),
                ('services', models.ManyToManyField(blank=True, to='hotels.service')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belu_auth.beluuserprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_paid', models.DateTimeField(blank=True, null=True)),
                ('last_four_digits', models.CharField(max_length=4)),
                ('payment_method', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.reservation')),
            ],
        ),
    ]