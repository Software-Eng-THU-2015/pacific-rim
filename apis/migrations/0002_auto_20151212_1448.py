# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banduser',
            old_name='bu_wechat_id',
            new_name='bu_openid',
        ),
        migrations.RemoveField(
            model_name='banduser',
            name='bu_user',
        ),
    ]
