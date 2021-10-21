"""Simple Unitesting for the word model."""

from django.test import TestCase
from rest_framework.serializers import ListSerializer
from ..serializers import SentenceSerializer
from ..models import Sentence
import logging

logger = logging.getLogger('spanglish')


class SentenceSerializerTestClass(TestCase):
    """Test the Sentence serializer"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")


    def test_get_single_serialized_sentence_success(self):
        """get a sentence model and serialize it. return a serializedsentence object back."""

        sentence_model = Sentence.objects.get(pk=1)
        sentence_serialized = SentenceSerializer(sentence_model, many=False)
        logger.debug("sentence_serialized %s" % type(sentence_serialized))

        # convert the serialized_sentence to a dict.
        sentence_data = sentence_serialized.data
        
        sentence_keys = list(sentence_data.keys())
        expected_fields = ['id', 'sentence', 'language', 'category', 'created']

        logger.debug("sentence_keys: %s", sentence_keys)

        self.assertIsInstance(sentence_serialized, SentenceSerializer)
        self.assertEqual(sorted(sentence_keys), sorted(expected_fields))


    def test_get_all_serialized_sentence_success(self):
        """get all sentence models and serialize them. return a list of serializedsentence objects back."""

        sentence_model = Sentence.objects.all()
        sentence_serialized = SentenceSerializer(sentence_model, many=True)
        logger.debug("sentence_serialized all %s" % type(sentence_serialized))

        self.assertIsInstance(sentence_serialized, ListSerializer)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")