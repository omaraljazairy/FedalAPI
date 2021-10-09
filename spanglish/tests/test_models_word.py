"""Simple Unitesting for the word model."""

from django.test import TestCase
from spanglish.models import Word
import logging

logger = logging.getLogger('spanglish')


class WordModelTestClass(TestCase):
    """Test the Word model"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")


    def test_create_word_object_success(self):
        """create a new word by providing the word, language and category"""

        word = Word.objects.create(word='Miercoles', language='2', category=3)
        word.save()
        logger.debug("word created %s" % word)

        self.assertEquals("Miercoles", word.word)


    def test_get_word_en(self):
        """get the 1st word and expect it to be Hablar"""

        word = Word.objects.get(pk=1)
        logger.debug("get word: %s" % Word.word)

        self.assertEquals(word.word, 'Hablar')


    def test_create_word_without_language_exception(self):
        """try to create a word object with no language. should throw an exception"""

        with self.assertRaises(expected_exception=Exception) as e:
            Word.object.create(word='Something', category=2).save()


    def test_applabel_word_spanglish(self):
        """expect the applabel to be spanglish."""

        word = Word.objects.get(pk=1)
        applabel = str(word._meta.app_label)

        logger.debug('applabel: %s' % applabel)

        self.assertEquals(applabel, 'spanglish')


    def test_update_word_code_success(self):
        """ update the category_id of the word to 2. expect no error. """

        word = Word.objects.get(pk=2)
        word.category = 2
        word.save()

        logger.debug("new category for the word %s is updated to %s", word.word, word.category)

        self.assertEqual(2, word.category)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")