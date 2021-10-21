"""Simple Unitesting for the word model."""

from django.test import TestCase
from rest_framework.serializers import ListSerializer
from ..serializers import WordSerializer
from ..models import Word
import logging

logger = logging.getLogger('spanglish')


class WordSerializerTestClass(TestCase):
    """Test the Word serializer"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")


    def test_get_single_serialized_word_success(self):
        """get a word model and serialize it. return a serializedword object back."""

        word_model = Word.objects.get(pk=1)
        word_serialized = WordSerializer(word_model, many=False)
        logger.debug("word_serialized %s" % type(word_serialized))

        # convert the serialized_word to a dict.
        word_data = word_serialized.data
        
        word_keys = list(word_data.keys())
        expected_fields = ['id', 'word', 'language', 'category', 'created']

        logger.debug("word_keys: %s", word_keys)

        self.assertIsInstance(word_serialized, WordSerializer)
        self.assertEqual(sorted(word_keys), sorted(expected_fields))


    def test_get_all_serialized_word_success(self):
        """get all word models and serialize them. return a list of serializedword objects back."""

        word_model = Word.objects.all()
        word_serialized = WordSerializer(word_model, many=True)
        logger.debug("word_serialized all %s" % type(word_serialized))

        self.assertIsInstance(word_serialized, ListSerializer)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")