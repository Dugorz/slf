# Generated by Django 2.2 on 2019-04-06 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190406_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workersmodel',
            old_name='portfolio',
            new_name='worker_portfolio',
        ),
    ]