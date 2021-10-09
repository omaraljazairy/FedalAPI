# Generated by Django 3.2.7 on 2021-09-27 20:23

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Category',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(db_column='code', max_length=2, unique=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Language',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=255, unique=True)),
                ('language', models.IntegerField(db_column='language_id')),
                ('category', models.IntegerField(db_column='category_id')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Sentence',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.IntegerField(blank=True, db_column='word_id', null=True)),
                ('sentence', models.IntegerField(blank=True, db_column='sentence_id', null=True)),
                ('language', models.IntegerField(db_column='language_id')),
                ('translation', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Translation',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tense', models.CharField(max_length=19)),
                ('word', models.IntegerField(db_column='word_id')),
                ('yo', models.CharField(blank=True, max_length=25, null=True)),
                ('tu', models.CharField(blank=True, max_length=25, null=True)),
                ('usted', models.CharField(blank=True, max_length=25, null=True)),
                ('nosotros', models.CharField(blank=True, max_length=25, null=True)),
                ('vosotros', models.CharField(blank=True, max_length=25, null=True)),
                ('ustedes', models.CharField(blank=True, max_length=25, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Verb',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=30, unique=True)),
                ('language', models.IntegerField(db_column='language_id')),
                ('category', models.IntegerField(db_column='category_id')),
                ('created', models.DateTimeField(auto_now=True, blank=True, null=True)),
            ],
            options={
                'db_table': 'Word',
                'managed': settings.IS_TESTING,
            },
        ),
    ]
