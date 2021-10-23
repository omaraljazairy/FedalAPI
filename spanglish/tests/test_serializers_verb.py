"""Simple Unitesting for the verb model."""

from django.test import TestCase
from rest_framework.serializers import ListSerializer
from ..serializers import VerbSerializer
from ..models import Verb
import logging

logger = logging.getLogger('spanglish')


class VerbSerializerTestClass(TestCase):
    """Test the Verb serializer"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")


    def test_get_single_serialized_verb_success(self):
        """get a verb model and serialize it. return a serializedverb object back."""

        verb_model = Verb.objects.get(pk=1)
        verb_serialized = VerbSerializer(verb_model, many=False)
        logger.debug("verb_serialized %s" % type(verb_serialized))

        # convert the serialized_verb to a dict.
        verb_data = verb_serialized.data
        
        verb_keys = list(verb_data.keys())
        expected_fields = [
            'id', 
            'tense', 
            'word', 
            'yo', 
            'tu', 
            'usted', 
            'nosotros', 
            'vosotros', 
            'ustedes', 
            'created'
        ]

        logger.debug("verb_keys: %s", verb_keys)

        self.assertIsInstance(verb_serialized, VerbSerializer)
        self.assertEqual(sorted(verb_keys), sorted(expected_fields))


    def test_get_all_serialized_verb_success(self):
        """get all verb models and serialize them. return a list of serializedverb objects back."""

        verb_model = Verb.objects.all()
        verb_serialized = VerbSerializer(verb_model, many=True)
        logger.debug("verb_serialized all %s" % type(verb_serialized))

        self.assertIsInstance(verb_serialized, ListSerializer)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")