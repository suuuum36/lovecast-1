# Generated by Django 2.2.3 on 2019-08-06 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0006_auto_20190806_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cloudy_posts',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nickname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='rainy_posts',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='sunny_posts',
        ),
    ]