# Generated by Django 2.2.7 on 2019-12-17 13:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('languages', '0003_auto_20191217_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('detail', models.TextField(blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discussions', to='languages.Language')),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discussionreport', to=settings.AUTH_USER_MODEL)),
                ('discussion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discussionreport', to='discussions.Discussion')),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussioncomments', to='discussions.Discussion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussioncomments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
