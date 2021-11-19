# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Category'


class Language(models.Model):
    name = models.CharField(unique=True, max_length=20)
    code = models.CharField(unique=True, max_length=2)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Language'


class Quiz(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    verb_tense = models.TextField(blank=True, null=True)
    quiz_type = models.CharField(max_length=10, blank=True, null=True)
    exclude_daily = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Quiz'


class Sentence(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    sentence = models.CharField(unique=True, max_length=255)
    language = models.ForeignKey(Language, models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Sentence'


class Translation(models.Model):
    word = models.ForeignKey(
        'Word', 
        models.DO_NOTHING,
        related_name='translations',
        blank=True, 
        null=True
    )
    sentence = models.ForeignKey(
        Sentence, 
        models.DO_NOTHING, 
        related_name='translations',
        blank=True, 
        null=True
    )
    language = models.ForeignKey(Language, models.DO_NOTHING)
    translation = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Translation'
        unique_together = (('sentence', 'translation'), ('word', 'translation'),)


class Verb(models.Model):
    tense = models.CharField(max_length=19)
    word = models.ForeignKey(
        'Word', 
        models.DO_NOTHING,
        related_name='verb',
        # related_query_name='verbword'
    )
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

    def __str__(self) -> str:
        return f"{self.id}: yo {self.yo} - tu {self.tu} - usted {self.usted} \
 - nosotros {self.nosotros} - vosotros {self.vosotros} - ustedes {self.ustedes}"


class Word(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, models.DO_NOTHING)
    word = models.CharField(unique=True, max_length=30)
    language = models.ForeignKey(Language, models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'Word'

    def __str__(self) -> str:
        return f"{self.word} - {self.language.name} - {self.category.name}"
