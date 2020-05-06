# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-05-04 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=30)),
                ('aphone', models.CharField(max_length=11)),
                ('addr', models.CharField(max_length=100)),
                ('isdefault', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('pwd', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Userinfo'),
        ),
    ]