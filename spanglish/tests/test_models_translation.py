"""Simple Unitesting for the translation model."""

from django.test import TestCase
from spanglish.models import Translation, Word, Sentence, Language
import logging

logger = logging.getLogger('spanglish')


class TranslationModelTestClass(TestCase):
    """Test the Translation model"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""
        
        logger.debug("setUpClass started")
        cls.language = Language.objects.get(pk=1)
        cls.word = Word.objects.get(pk=2)
        cls.sentence = Sentence.objects.get(pk=2)


    def test_create_translation_object_word_success(self):
        """create a new translation by providing the translation, language and word."""

        translation = Translation.objects.create(
            translation='Hello', 
            language=self.language, 
            word=self.word
        )
        translation.save()
        logger.debug("translation created %s" % translation)

        self.assertEquals("Hello", translation.translation)


    def test_create_translation_object_sentence_success(self):
        """create a new translation by providing the translation, language and sentence."""

        translation = Translation.objects.create(
            translation='Where are you from ?', 
            language=self.language, 
            sentence=self.sentence
        )
        translation.save()
        logger.debug("translation created %s" % translation)

        self.assertEquals("Where are you from ?", translation.translation)


    def test_get_translation_en(self):
        """get the translations with language en"""

        translation = Translation.objects.filter(language=1).values()
        logger.debug("get translation: %s" % translation)

        self.assertTrue(len(translation) > 1)


    def test_create_translation_without_language_exception(self):
        """try to create a translation object with no language. should throw an exception"""

        with self.assertRaises(expected_exception=Exception) as e:
            Translation.object.create(word=self.word, translation='bar').save()

        logger.debug("expection thrown")


    def test_applabel_translation_spanglish(self):
        """expect the applabel to be spanglish."""

        translation = Translation.objects.get(pk=1)
        applabel = str(translation._meta.app_label)

        logger.debug('applabel: %s' % applabel)

        self.assertEquals(applabel, 'spanglish')


    def test_update_translation_translation_success(self):
        """ update the translation of the translation. expect no error. """

        translation = Translation.objects.get(pk=1)
        translation.translation = 'Speak'
        translation.save()

        logger.debug("new translation for the translation id %s is updated to %s", translation.id, translation.translation)

        self.assertEqual('Speak', translation.translation)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")