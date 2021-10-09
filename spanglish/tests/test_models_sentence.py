"""Simple Unitesting for the sentence model."""

from django.test import TestCase
from spanglish.models import Sentence
import logging

logger = logging.getLogger('spanglish')


class SentenceModelTestClass(TestCase):
    """Test the sentence model"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        logger.debug("setUpClass started")


    def test_create_sentence_object_success(self):
        """create a new sentence by providing the sentence, language and category"""

        sentence = Sentence.objects.create(sentence='Donde estas ?', language='2', category=2)
        sentence.save()
        logger.debug("sentence created %s" % sentence)

        self.assertEquals('Donde estas ?', sentence.sentence)


    def test_get_sentence(self):
        """get the 1st sentence and expect it to be Como estas"""

        sentence = Sentence.objects.get(pk=1)
        logger.debug("get sentence: %s" % sentence.sentence)

        self.assertEquals(sentence.sentence, 'Como estas ?')


    def test_create_sentence_without_language_exception(self):
        """try to create a sentence object with no language. should throw an exception"""

        with self.assertRaises(expected_exception=Exception) as e:
            Sentence.object.create(sentence='Something', category=2).save()


    def test_applabel_sentence_spanglish(self):
        """expect the applabel to be spanglish."""

        sentence = Sentence.objects.get(pk=1)
        applabel = str(sentence._meta.app_label)

        logger.debug('applabel: %s' % applabel)

        self.assertEquals(applabel, 'spanglish')


    def test_update_sentence_code_success(self):
        """ update the category_id of the sentence to 1. expect no error. """

        sentence = Sentence.objects.get(pk=1)
        sentence.category = 1
        sentence.save()

        logger.debug("new category for the sentence %s is updated to %s", sentence.sentence, sentence.category)

        self.assertEqual(1, sentence.category)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")