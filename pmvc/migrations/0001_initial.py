# Generated by Django 2.2.4 on 2019-08-22 12:49

from django.db import migrations, models
import django.db.models.deletion
import pmvc.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Work Order', max_length=30)),
                ('description', models.TextField()),
                ('digital_master', models.FileField(blank=True, null=True, upload_to=pmvc.models.account_video_media_directory_path)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pmvc.Account')),
            ],
        ),
    ]
