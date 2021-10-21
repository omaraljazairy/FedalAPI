"""Simple Unitesting for the word model."""

from django.test import TestCase
from rest_framework.serializers import ListSerializer
from ..serializers import LanguageSerializer
from ..models import Language
import logging

logger = logging.getLogger('spanglish')


class LanguageSerializerTestClass(TestCase):
    """Test the Language serializer"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")


    def test_get_single_serialized_language_success(self):
        """get a language model and serialize it. return a serializedlanguage object back."""

        language_model = Language.objects.get(pk=1)
        language_serialized = LanguageSerializer(language_model, many=False)
        logger.debug("language_serialized %s" % type(language_serialized))

        # convert the serialized_language to a dict.
        language_data = language_serialized.data
        
        language_keys = list(language_data.keys())
        expected_fields = ['id', 'name', 'code', 'created']

        logger.debug("language_keys: %s", language_keys)

        self.assertIsInstance(language_serialized, LanguageSerializer)
        self.assertEqual(sorted(language_keys), sorted(expected_fields))


    def test_get_all_serialized_language_success(self):
        """get all language models and serialize them. return a list of serializedlanguage objects back."""

        language_model = Language.objects.all()
        language_serialized = LanguageSerializer(language_model, many=True)
        logger.debug("language_serialized all %s" % type(language_serialized))

        self.assertIsInstance(language_serialized, ListSerializer)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")