# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-20 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patchwork', '0027_auto_20180116_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmation',
            name='type',
            field=models.CharField(choices=[('userperson', 'User-Person association'), ('registration', 'Registration'), ('optout', 'Email opt-out')], max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='subject_prefix_tags',
            field=models.CharField(blank=True, help_text='Comma separated list of tags', max_length=255),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(default='Series without cover letter', max_length=200),
        ),
        migrations.AlterField(
            model_name='seriesrevision',
            name='state',
            field=models.SmallIntegerField(choices=[(0, 'incomplete'), (1, 'initial'), (2, 'in progress'), (3, 'done')], default=0),
        ),
        migrations.AlterField(
            model_name='seriesrevision',
            name='test_state',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'pending'), (1, 'info'), (2, 'success'), (3, 'warning'), (4, 'failure')], null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='abbrev',
            field=models.CharField(help_text='Short (one-or-two letter) abbreviation for the tag, used in table column headers', max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='pattern',
            field=models.CharField(help_text='A simple regex to match the tag in the content of a message. Will be used with MULTILINE and IGNORECASE flags. eg. ^Acked-by:', max_length=50),
        ),
        migrations.AlterField(
            model_name='test',
            name='mail_cc_list',
            field=models.CharField(blank=True, help_text='Comma separated list of emails', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='mail_condition',
            field=models.SmallIntegerField(choices=[(0, 'always'), (1, 'on warning/failure'), (2, 'on failure')], default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='mail_recipient',
            field=models.SmallIntegerField(choices=[(0, 'none'), (1, 'submitter'), (2, 'mailing list'), (3, 'recipient list')], default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='mail_to_list',
            field=models.CharField(blank=True, help_text='Comma separated list of emails', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='state',
            field=models.SmallIntegerField(choices=[(0, 'pending'), (1, 'info'), (2, 'success'), (3, 'warning'), (4, 'failure')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='patches_per_page',
            field=models.PositiveIntegerField(default=100, help_text='Number of patches to display per page'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='send_email',
            field=models.BooleanField(default=False, help_text='Selecting this option allows patchwork to send email on your behalf'),
        ),
    ]