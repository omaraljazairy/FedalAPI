"""Simple Unitesting for the word model."""

from django.test import TestCase
from rest_framework.serializers import ListSerializer
from ..serializers import TranslationSerializer
from ..models import Translation
import logging

logger = logging.getLogger('spanglish')


class TranslationSerializerTestClass(TestCase):
    """Test the Translation serializer"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")


    def test_get_single_serialized_translation_success(self):
        """get a translation model and serialize it. return a serializedtranslation object back."""

        translation_model = Translation.objects.get(pk=1)
        translation_serialized = TranslationSerializer(translation_model, many=False)
        logger.debug("translation_serialized %s" % type(translation_serialized))

        # convert the serialized_translation to a dict.
        translation_data = translation_serialized.data
        
        translation_keys = list(translation_data.keys())
        expected_fields = ['id', 'word', 'sentence', 'language', 'languagename', 'translation', 'created']

        logger.debug("translation_keys: %s", translation_keys)

        self.assertIsInstance(translation_serialized, TranslationSerializer)
        self.assertEqual(sorted(translation_keys), sorted(expected_fields))


    def test_get_all_serialized_translation_success(self):
        """get all translation models and serialize them. return a list of serializedtranslation objects back."""

        translation_model = Translation.objects.all()
        translation_serialized = TranslationSerializer(translation_model, many=True)
        logger.debug("translation_serialized all %s" % type(translation_serialized))

        self.assertIsInstance(translation_serialized, ListSerializer)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")