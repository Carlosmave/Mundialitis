# Generated by Django 2.0.2 on 2018-02-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mundialitisapps', '0019_partido_resultado'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='identifier',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]