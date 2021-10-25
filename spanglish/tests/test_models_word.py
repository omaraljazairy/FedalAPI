"""Simple Unitesting for the word model."""

from django.test import TestCase
from spanglish.models import Word, Category, Language
from django.contrib.auth.models import User
import logging

logger = logging.getLogger('spanglish')


class WordModelTestClass(TestCase):
    """Test the Word model"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")
        cls.category = Category.objects.get(pk=3)
        cls.language = Language.objects.get(pk=2)
        cls.user = User.objects.get(pk=1)


    def test_create_word_object_success(self):
        """create a new word by providing the word, language and category"""

        word = Word.objects.create(
            word='Miercoles', 
            language=self.language, 
            category=self.category,
            user=self.user
        )
        word.save()
        logger.debug("word created %s" % word)

        self.assertEquals("Miercoles", word.word)


    def test_get_word_en(self):
        """get the 1st word and expect it to be Hablar"""

        word = Word.objects.get(pk=1)
        logger.debug("get word: %s" % word)

        self.assertEquals(word.word, 'Hablar')


    def test_create_word_without_language_exception(self):
        """try to create a word object with no language. should throw an exception"""

        with self.assertRaises(expected_exception=Exception) as e:
            Word.object.create(word='Something', category=self.category, user=self.user).save()


    def test_applabel_word_spanglish(self):
        """expect the applabel to be spanglish."""

        word = Word.objects.get(pk=1)
        applabel = str(word._meta.app_label)

        logger.debug('applabel: %s' % applabel)

        self.assertEquals(applabel, 'spanglish')


    def test_update_word_code_success(self):
        """ update the category_id of the word to 2. expect no error. """

        word = Word.objects.get(pk=2)
        word.word = 'something new'
        word.save()

        logger.debug("word_Id %s is updated to %s", word.id, word.word)

        self.assertEqual('something new', word.word)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")