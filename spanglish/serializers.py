import logging
from rest_framework import serializers
from .models import Category, Language, Word, Sentence, Translation, Verb

logger = logging.getLogger('spanglish')


class CategorySerializer(serializers.ModelSerializer):
    """Serialize the Catgory model object."""

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Category
        fields = '__all__' 
        # ('id', 'url', 'name', 'created')


class LanguageSerializer(serializers.ModelSerializer):
    """Serialize the Language model object."""

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Language
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    """Serialize the Word model object."""

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Word
        fields = '__all__'


class SentenceSerializer(serializers.ModelSerializer):
    """Serialize the Sentence model object."""

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Sentence
        fields = '__all__'


class VerbSerializer(serializers.ModelSerializer):
    """Serialize the Verb model object."""

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Verb
        fields = '__all__'

class TranslationSerializer(serializers.ModelSerializer):
    """Serialize the Translation model object."""

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Translation
        fields = '__all__'
