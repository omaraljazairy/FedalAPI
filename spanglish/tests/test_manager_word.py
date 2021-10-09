# from django.test import TestCase
# from spanglish.managers.wordmanager import WordManager
# import logging

# logger = logging.getLogger('spanglish')


# class WordManagerTestClass(TestCase):
#     """Test the word manager"""

#     @classmethod
#     def setUpClass(cls):
#         """Run at the start of the test of this class."""
#         logger.debug("setUpClass started")

    
#     def test_get_all_words_by_language_code(self):
#         """provide the language code to the manager and expect to get back 
#         all words with language id 2.
#         """

#         words = WordManager.get_words_by_language_id(language_id=2)
#         logger.debug('words returned: %s', words)
#         logger.debug('total words: %s', len(words))

#         self.assertTrue(len(words) > 1)

    
#     def test_get_all_words_by_category(self):
#         """provide the category id 2 to the manager and expect to get back 
#         all words with category id 2.
#         """

#         words = WordManager.get_words_by_category_code(category_id=2)
#         logger.debug('words returned: %s', words)
#         logger.debug('total words: %s', len(words))

#         self.assertTrue(len(words) > 1)






#     @classmethod
#     def tearDownClass(cls):
#         """Run after all tests are done."""
#         logger.debug("tearDownClass started")
