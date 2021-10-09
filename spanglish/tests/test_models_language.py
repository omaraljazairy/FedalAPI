"""Simple Unitesting for the Language model."""

from django.test import TestCase
from spanglish.models import Language
import logging

logger = logging.getLogger('spanglish')


class LanguageModelTestClass(TestCase):
    """Test the Language model"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")


    def test_create_language_object_success(self):
        """create a new language by providing the name and ios1"""

        language_fr = Language.objects.create(name='French', code='fr')
        language_fr.save()
        logger.debug("language_fr created %s" % language_fr)

        self.assertEquals("French", language_fr.name)


    def test_get_language_en(self):
        """get the 1st language iso1 and expect it to be en"""

        language_en = Language.objects.get(pk=1)
        logger.debug("language_en: %s" % language_en)
        logger.debug("language_en iso1: %s" % language_en.code)

        self.assertEquals(language_en.code, 'en')


    def test_create_language_without_code_exception(self):
        """try to create a language object with no iso1. should throw an exception"""

        with self.assertRaises(expected_exception=Exception) as e:
            Language.object.create(name='Swedish').save()


    def test_applabel_language_spanglish(self):
        """expect the applabel to be spanglish."""

        langauge = Language.objects.get(pk=1)
        applabel = str(langauge._meta.app_label)

        logger.debug('applabel: %s' % applabel)

        self.assertEquals(applabel, 'spanglish')


    def test_update_language_code_success(self):
        """ update the code of the en language to ee. expect no error. """

        language = Language.objects.get(pk=1)
        language.code = 'ee'
        language.save()

        logger.debug("new EN language updated to %s", language.code)

        self.assertEqual('ee', language.code)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")