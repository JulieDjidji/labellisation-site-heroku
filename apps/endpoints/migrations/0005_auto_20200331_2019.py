# Generated by Django 3.0.4 on 2020-03-31 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0004_auto_20200316_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='label',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='prediction',
            field=models.FloatField(),
        ),
    ]
