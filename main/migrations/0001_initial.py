# Generated by Django 2.2 on 2019-04-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=50, verbose_name='Worker name')),
                ('worker', models.ImageField(upload_to='', verbose_name='Worker portrait')),
                ('slug', models.SlugField()),
                ('portfolio', models.ImageField(upload_to='', verbose_name='Worker portfolio')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Worker',
                'verbose_name_plural': 'Workers',
            },
        ),
    ]
