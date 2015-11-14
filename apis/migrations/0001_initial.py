# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BandUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('bu_band', models.IntegerField()),
                ('bu_wechat_id', models.CharField(max_length=128)),
                ('bu_gender', models.IntegerField()),
                ('bu_birthday', models.DateTimeField()),
                ('bu_height', models.IntegerField()),
                ('bu_weight', models.IntegerField()),
                ('bu_follow', models.ManyToManyField(related_name='bu_follow', to=settings.AUTH_USER_MODEL)),
                ('bu_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('he_id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('he_time', models.DateTimeField()),
                ('he_pressure', models.IntegerField()),
                ('he_heart_rate', models.IntegerField()),
                ('he_user', models.ForeignKey(related_name='he_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('pl_id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('pl_time_from', models.DateTimeField()),
                ('pl_time_to', models.DateTimeField()),
                ('pl_time', models.TimeField()),
                ('pl_goal', models.CharField(max_length=128)),
                ('pl_description', models.TextField()),
                ('pl_user', models.ForeignKey(related_name='pl_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('sl_id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('sl_time_from', models.DateTimeField()),
                ('sl_time_to', models.DateTimeField()),
                ('sl_length', models.TimeField()),
                ('sl_deep_length', models.TimeField()),
                ('sl_user', models.ForeignKey(related_name='sl_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('st_id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('st_time', models.DateTimeField()),
                ('st_step_number', models.IntegerField()),
                ('st_calorie', models.IntegerField()),
                ('st_distance', models.IntegerField()),
                ('st_user', models.ForeignKey(related_name='st_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tg_id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('tg_time_from', models.DateTimeField()),
                ('tg_time_to', models.DateTimeField()),
                ('tg_content', models.ForeignKey(related_name='tg_content', to=settings.AUTH_USER_MODEL)),
                ('tg_user', models.ForeignKey(related_name='tg_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TagContent',
            fields=[
                ('tc_id', models.AutoField(unique=True, serialize=False, primary_key=True)),
                ('tc_content', models.CharField(max_length=128)),
                ('tc_user', models.ForeignKey(related_name='tc_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
