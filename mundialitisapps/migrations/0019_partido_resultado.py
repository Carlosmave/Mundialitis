# Generated by Django 2.0.2 on 2018-02-23 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundialitisapps', '0018_auto_20180222_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='resultado',
            field=models.TextField(default='Empate'),
            preserve_default=False,
        ),
    ]
