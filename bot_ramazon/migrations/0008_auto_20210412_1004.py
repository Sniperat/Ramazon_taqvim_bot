# Generated by Django 3.1.7 on 2021-04-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_ramazon', '0007_duolar'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='is_plus',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='region',
            name='reg_asr',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='reg_bamdod',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='reg_peshin',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='reg_shom',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='reg_tong',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='reg_xufton',
            field=models.TimeField(null=True),
        ),
    ]
