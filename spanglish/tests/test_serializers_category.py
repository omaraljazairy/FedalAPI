"""Simple Unitesting for the word model."""

from django.test import TestCase, RequestFactory
from rest_framework.serializers import ListSerializer
from ..serializers import CategorySerializer
from ..models import Category
import logging

logger = logging.getLogger('spanglish')


class CategorySerializerTestClass(TestCase):
    """Test the Category serializer"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")
        requestFactory = RequestFactory()
        cls.request = requestFactory.get('/')


    def test_get_single_serialized_category_success(self):
        """get a category model and serialize it. return a serializedcategory object back."""

        category_model = Category.objects.get(pk=1)
        category_serialized = CategorySerializer(category_model, context={'request': self.request}, many=False)
        logger.debug("category_serialized %s" % type(category_serialized))

        # convert the serialized_category to a dict.
        category_data = category_serialized.data
        
        category_keys = list(category_data.keys())
        expected_fields = ['id', 'name', 'created']

        logger.debug("category_keys: %s", category_keys)

        self.assertIsInstance(category_serialized, CategorySerializer)
        self.assertEqual(sorted(category_keys), sorted(expected_fields))


    def test_get_all_serialized_category_success(self):
        """get all category models and serialize them. return a list of serializedcategory objects back."""

        category_model = Category.objects.all()
        category_serialized = CategorySerializer(category_model, many=True)
        logger.debug("category_serialized all %s" % type(category_serialized))

        self.assertIsInstance(category_serialized, ListSerializer)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")