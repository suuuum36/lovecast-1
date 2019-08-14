# Generated by Django 2.2.3 on 2019-08-14 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0039_auto_20190814_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='photo',
        ),
        migrations.AddField(
            model_name='photos',
            name='feed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedpage.Feed'),
        ),
    ]
