# Generated by Django 2.2.3 on 2019-08-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0008_auto_20190806_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='cloudy_content',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='feed',
            name='rainy_content',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='feed',
            name='sunny_content',
            field=models.CharField(max_length=256),
        ),
    ]