# Generated by Django 3.2.9 on 2021-11-30 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20211129_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbooking',
            name='date',
        ),
    ]
