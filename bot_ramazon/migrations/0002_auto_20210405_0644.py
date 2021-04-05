# Generated by Django 3.1.7 on 2021-04-05 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot_ramazon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='region',
        ),
        migrations.AddField(
            model_name='user',
            name='region_ID',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bot_ramazon.region'),
        ),
    ]
