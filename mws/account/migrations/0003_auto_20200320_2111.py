# Generated by Django 3.0.3 on 2020-03-20 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200320_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password1',
            new_name='password',
        ),
    ]