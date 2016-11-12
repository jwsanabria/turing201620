# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-02 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sonidosLibresApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='audio',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='audio',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='relatedCategories',
            field=models.ManyToManyField(blank=True, editable=False, related_name='_category_relatedCategories_+', to='sonidosLibresApp.Category'),
        ),
        migrations.AlterField(
            model_name='convocation',
            name='dateEnd',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='convocation',
            name='dateInit',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='convocation',
            name='dateLimit',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='convocation',
            name='dateResults',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='convocation',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='convocation',
            name='terms',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='convocation',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='convocationaudio',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
