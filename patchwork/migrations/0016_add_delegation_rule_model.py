# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patchwork', '0015_remove_version_n_patches'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelegationRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.CharField(max_length=255)),
                ('priority', models.IntegerField(default=0)),
                ('project', models.ForeignKey(to='patchwork.Project', on_delete=models.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['-priority', 'path'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='delegationrule',
            unique_together=set([('path', 'project')]),
        ),
    ]
