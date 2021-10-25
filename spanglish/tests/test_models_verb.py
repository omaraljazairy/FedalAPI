"""Simple Unitesting for the verb model."""

from django.test import TestCase
from spanglish.models import Verb, Word
import logging

logger = logging.getLogger('spanglish')


class VerbModelTestClass(TestCase):
    """Test the verb model"""

    @classmethod
    def setUpClass(cls):
        """Run at the start of the test of this class."""

        logger.debug("setUpClass started")
        cls.word = Word.objects.get(pk=3)


    def test_create_verb_object_success(self):
        """create a new verb by providing all required fields. expect the word to be created. """

        verb = Verb.objects.create(
            tense='present', 
            word=self.word, 
            yo='voy', 
            tu='vas', 
            usted='va', 
            nosotros='vamos', 
            vosotros='vais', 
            ustedes='van'
        )
        verb.save()
        logger.debug("verb created %s" % verb)

        self.assertEquals("vamos", verb.nosotros)


    def test_get_verb_hablo(self):
        """get the 1st verb and expect it to be Hablo"""

        verb = Verb.objects.get(pk=1)
        logger.debug("get verb: %s" % verb.yo)

        self.assertEquals(verb.yo, 'hablo')


    def test_create_verb_without_word_exception(self):
        """try to create a verb object with a word. should throw an exception"""

        with self.assertRaises(expected_exception=Exception) as e:
            Verb.object.create(
                tense='present', 
                yo='something', 
                tu='something', 
                usted='something', 
                nosotros='something', 
                vosotros='something', 
                ustedes='something').save()


    def test_applabel_verb_spanglish(self):
        """expect the applabel to be spanglish."""

        verb = Verb.objects.get(pk=1)
        applabel = str(verb._meta.app_label)

        logger.debug('applabel: %s' % applabel)

        self.assertEquals(applabel, 'spanglish')


    def test_update_verb_code_success(self):
        """ update the tense of the verb to past. expect no error. """

        verb = Verb.objects.get(pk=1)
        verb.tense = 'past'
        verb.save()

        logger.debug("new tense for the verb %s is updated to %s", verb.yo, verb.tense)

        self.assertEqual('past', verb.tense)


    @classmethod
    def tearDownClass(cls):
        """Run after all tests are done."""
        logger.debug("tearDownClass started")