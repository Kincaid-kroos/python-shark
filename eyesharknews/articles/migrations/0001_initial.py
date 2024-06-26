# Generated by Django 5.0.3 on 2024-03-27 19:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('category', models.CharField(choices=[('sports', 'Sports'), ('entertainment', 'Entertainment'), ('tech', 'Tech'), ('business', 'Business'), ('politics', 'Politics'), ('worldnews', 'Worldnews'), ('more', 'More')], default='business', max_length=50)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('featured', models.BooleanField(default=False)),
                ('latest', models.BooleanField(default=False)),
                ('popular', models.BooleanField(default=False)),
                ('hero', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
