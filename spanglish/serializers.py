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



class VerbSerializer(serializers.ModelSerializer):
    """Serialize the Verb model object."""

    # something = serializers.ReadOnlyField(source='word.word')
    

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Verb
        fields = '__all__'

class TranslationSerializer(serializers.ModelSerializer):
    """Serialize the Translation model object."""

    languagename = serializers.ReadOnlyField(source='language.name')
    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Translation
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    """Serialize the Word model object."""

    verb = serializers.StringRelatedField(many=True, read_only=True)
    # languagename = serializers.ReadOnlyField(source='language.name')
    # language = serializers.PrimaryKeyRelatedField(
    #     queryset=Word.objects.all(),
    #     required=False,
    #     write_only=True
    # )

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Word
        fields = '__all__'
        # fields = [
        #     'id',
        #     'word',
        #     'user',
        #     'languagename',
        #     'language',
        #     'category',
        #     'verb'
        # ]

        # exclude = ('language',)
        # depth = 1

class WordDetailsSerializer(serializers.ModelSerializer):
    """Serialize the Word model object only for representation. no post or put. """

    verb = VerbSerializer(many=True, read_only=True)
    language = serializers.ReadOnlyField(source='language.name')
    category = serializers.ReadOnlyField(source='category.name')
    translations = TranslationSerializer(many=True, read_only=True)
    # language = serializers.PrimaryKeyRelatedField(
    #     queryset=Word.objects.all(),
    #     required=False,
    #     write_only=True
    # )

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Word
        fields = [
            'id',
            'created',
            'word',
            'user',
            'language',
            'translations',
            'category',
            'verb'
        ]

        # exclude = ('language',)
        # depth = 1


class SentenceSerializer(serializers.ModelSerializer):
    """Serialize the Sentence model object."""

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Sentence
        fields = '__all__'


class SentenceDetailsSerializer(serializers.ModelSerializer):
    """Serialize the Sentence model object only for representation. no post or put. """

    language = serializers.ReadOnlyField(source='language.name')
    category = serializers.ReadOnlyField(source='category.name')
    translations = TranslationSerializer(many=True, read_only=True)

    class Meta:
        """specify which fields should be serialized. in this case, all. """

        model = Sentence
        fields = [
            'id',
            'created',
            'sentence',
            'user',
            'language',
            'translations',
            'category'
        ]

