"""Unitests for the views classes and functions"""

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission, Group
from spanglish.models import Translation
import logging

logger = logging.getLogger('spanglish')


class TranslationViewTestClass(TestCase):
    """Translation view tests."""

    @classmethod
    def setUpClass(cls):
        """Create a test user & group with the specific permission.
        initalize the client and apiclient.
        """
        logger.debug("%s started " % cls.__name__)
        cls.api_url = 'http://127.0.0.1:8002/spanglish/translation/'
        cls.api_url2 = 'http://127.0.0.1:8002/spanglish/translations/'

        # create permissions
        # first get the contenttype of the model
        content_type = ContentType.objects.get_for_model(Translation)
        add_permission, created = Permission.objects.get_or_create(
            codename='add_translation',
            name='Can add translation',
            content_type=content_type
        )
        change_permission, created = Permission.objects.get_or_create(
            codename='change_translation',
            name='Can change translation',
            content_type=content_type
        )
        delete_permission, created = Permission.objects.get_or_create(
            codename='delete_translation',
            name='Can delete translation',
            content_type=content_type
        )

        # authenticated user
        username = 'translation_tester'
        passsword = 'test1234'
        email = 'translation_tester@fedla.net'
        groupName = 'Spanglish'

        # unauthenticated user
        username2 = 'translation_tester2'
        passsword2 = 'test12342'
        email2 = 'translation_tester2@fedla.net'
        groupName2 = 'Spanglish2'

        # create users
        user = User.objects.create_user(username=username, email=email, password=passsword)
        user2 = User.objects.create_user(username=username2, email=email2, password=passsword2)
        logger.debug("user created: %s" % user)
        logger.debug("user2 created: %s" % user2)

        # create groups
        group, created = Group.objects.get_or_create(name=groupName)
        group2, created2 = Group.objects.get_or_create(name=groupName2)
        logger.debug("group: %s created: %s" % (group, created))
        logger.debug("group2: %s created: %s" % (group2, created2))

        # add user to the group
        group.user_set.add(user)
        group2.user_set.add(user2)

        # add permissings to group
        group.permissions.add(add_permission)
        group.permissions.add(delete_permission)
        group.permissions.add(change_permission)

        # create the apiclient object
        cls.api_client = APIClient(enforce_csrf_checks=True)
        cls.api_client2 = APIClient(enforce_csrf_checks=True)

        # get token for the user1 and user2
        request = cls.api_client.post(
            '/api/token/',
            {
                'username': username,
                'password': passsword
            },
            format='json'
        )

        response = request.json()
        logger.debug("response for authentication: %s", response)

        # # token
        token = response['access']

        # # add the token to the api_client header
        cls.api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


    def test_view_get_all_translations_200(self):
        """test the get request to the api, expects 200 response with
        content."""

        # set the url for the api with param
        uri = self.api_url2
        response = self.api_client.get(uri) # make the request
        status_code = response.status_code
        content = response.json()

        logger.debug("response: %s" % response)
        logger.debug("content: %s" % content)

        self.assertEquals(status_code, 200)
        self.assertTrue(content)


    def test_view_get_translation_error_with_unknow_param_404(self):
        """test the get request to the api with an unknown param,
        expects 404 response with content."""

        # set the url for the api with param
        uri = self.api_url + 'all/'
        response = self.api_client.get(uri) # make the request
        status_code = response.status_code

        logger.debug("response: %s" % response)

        self.assertEquals(status_code, 404)


    def test_view_get_translation_with_content(self):
        """test the get request to the api to get translation id 1.
        expects 200 response with content json value to match
        the name Verb."""

        # set the url for the api with param
        uri = f'{self.api_url}1/'
        response = self.api_client.get(uri) # make the request
        status_code = response.status_code
        content = response.json()

        logger.debug("response content: %s" % content)

        expected_content = {
            "id": 1,
            "language": 1,
            "languagename": "English",
            "word": 1,
            "sentence": None,
            "created": "2021-09-28 13:35:51+0200",
            "translation": "Speak"
        }

        self.assertEquals(status_code, 200)
        self.assertDictEqual(d1=content, d2=expected_content)


    def test_view_create_translation_word_201(self):
        """post request to create a new translation for a word, expect to get back statuscode 201"""

        data = {
            "language": 1,
            "word": 2,
            "sentence": '',
            "translation": "Hello"
        }
        response = self.api_client.post(self.api_url2, data=data)
        status_code = response.status_code
        content = response.content

        logger.debug("response: %s" % response)
        logger.debug("content: %s" % content)

        self.assertEquals(201, status_code)


    def test_view_create_translation_sentence_201(self):
        """post request to create a new translation for a sentence, expect to get back statuscode 201"""

        data = {
            "language": 1,
            "sentence": 2,
            "word": '',
            "translation": "Where are you from"
        }
        response = self.api_client.post(self.api_url2, data=data)
        status_code = response.status_code
        content = response.content

        logger.debug("response: %s" % response)
        logger.debug("content: %s" % content)

        self.assertEquals(201, status_code)


    def test_view_put_translation_200(self):
        """update a translation by calling the patch action. expects response 200"""

        uri = f'{self.api_url}2/'
        data = {'language': 1, 'translation': 'Something to be translated'}

        response = self.api_client.patch(uri, data=data)
        status_code = response.status_code
        content = response.content

        logger.debug("response: %s" % response)
        logger.debug("content: %s" % content)

        self.assertEquals(200, status_code)


    def test_view_delete_translation_204(self):
        """delete a translation and expect 204"""

        uri = f'{self.api_url}2/'
        response = self.api_client.delete(uri, data={})
        status_code = response.status_code

        logger.debug("response: %s" % response.content)

        self.assertEquals(204, status_code)


    @classmethod
    def tearDownClass(cls):
        """remove the user and the group"""

        Permission.objects.all().delete()
        Group.objects.all().delete()
        # User.objects.all().delete()