# Generated by Django 3.1.7 on 2021-04-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_ramazon', '0003_user_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Namoz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bamdod', models.TimeField()),
                ('tong', models.TimeField()),
                ('peshin', models.TimeField()),
                ('asr', models.TimeField()),
                ('shom', models.TimeField()),
                ('xufton', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='note_asr',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='note_babdod',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='note_peshin',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='note_shom',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='note_tong',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='note_xufton',
            field=models.SmallIntegerField(default=0),
        ),
    ]
