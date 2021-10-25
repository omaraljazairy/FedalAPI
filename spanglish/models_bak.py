# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


APP_LABEL = 'spanglish'

class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Category'
        app_label = APP_LABEL


class Language(models.Model):
    name = models.CharField(unique=True, max_length=20)
    code = models.CharField(db_column='code', unique=True, null=True, max_length=2)  # Field renamed to remove unsuitable characters.
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Language'
        app_label = APP_LABEL


class Sentence(models.Model):
    sentence = models.CharField(unique=True, max_length=255)
    language = models.IntegerField(db_column='language_id',
                                     blank=False, null=False)
    category = models.IntegerField(db_column='category_id',
                                     blank=False, null=False)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Sentence'
        app_label = APP_LABEL


class Translation(models.Model):
    word = models.IntegerField(db_column='word_id',
                                     blank=True, null=True)
    sentence = models.IntegerField(db_column='sentence_id',
                                     blank=True, null=True)
    language = models.IntegerField(db_column='language_id',
                                     blank=False, null=False)
    translation = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Translation'
        app_label = APP_LABEL

class Verb(models.Model):
    tense = models.CharField(max_length=19)
    word = models.IntegerField(db_column='word_id',
                                     blank=False, null=False)
    yo = models.CharField(max_length=25, blank=True, null=True)
    tu = models.CharField(max_length=25, blank=True, null=True)
    usted = models.CharField(max_length=25, blank=True, null=True)
    nosotros = models.CharField(max_length=25, blank=True, null=True)
    vosotros = models.CharField(max_length=25, blank=True, null=True)
    ustedes = models.CharField(max_length=25, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Verb'
        unique_together = (('tense', 'word'),)
        app_label = APP_LABEL

class Word(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    word = models.CharField(unique=True, max_length=30)
    language = models.IntegerField(db_column='language_id',
                                     blank=False, null=False)
    category = models.IntegerField(db_column='category_id',
                                     blank=False, null=False)
    created = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Word'
        app_label = APP_LABEL
