# Generated by Django 3.0.4 on 2020-04-02 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0008_auto_20200401_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='labellisation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mlalgorithm',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mlalgorithmstatus',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mlrequest',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
