# Generated by Django 2.0.2 on 2018-02-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundialitisapps', '0012_auto_20180219_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='lobby',
            name='lstatus',
            field=models.CharField(default='No Iniciado', max_length=200),
            preserve_default=False,
        ),
    ]
