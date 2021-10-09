"""Simple Unitesting for the category model."""

from django.test import TestCase
from spanglish.models import Category
import logging

logger = logging.getLogger('spanglish')


class CategoryModelTestClass(TestCase):
    """Test the Category model"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")


    def test_create_category_object_success(self):
        """create a new category by providing the name and ios1"""

        category = Category.objects.create(name='numbers')
        category.save()
        logger.debug("category numbers is created %s" % category)

        self.assertEquals("numbers", category.name)

    
    def test_get_category_success(self):
        """get the 1st category and expect it to be verb"""

        category = Category.objects.get(pk=1)
        logger.debug("category: %s" % category)
        logger.debug("category name: %s" % category.name)

        self.assertEquals(category.name, 'verb')


    def test_create_category_without_name_exception(self):
        """try to create a category object with no name. should throw an exception"""

        with self.assertRaises(expected_exception=Exception) as e:
            Category.object.create().save()
        
        logger.debug("exception thrown")


    def test_applabel_category_spanglish(self):
        """expect the applabel to be spanglish."""

        category = Category.objects.get(pk=1)
        applabel = str(category._meta.app_label)

        logger.debug('applabel: %s' % applabel)

        self.assertEquals(applabel, 'spanglish')


    def test_update_category_code_success(self):
        """ update the code of the en category to ee. expect no error. """

        category = Category.objects.get(pk=1)
        category.name = 'verb2'
        category.save()

        logger.debug("new verb2 category updated to %s", category.name)

        self.assertEqual('verb2', category.name)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")