"""Unitests for the views classes and functions"""

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Permission, Group
from spanglish.models import Word
import logging

logger = logging.getLogger('spanglish')


class WordViewTestClass(TestCase):
    """Wordlist view tests."""

    @classmethod
    def setUpClass(cls):
        """Create a test user & group with the specific permission.
        initalize the client and apiclient.
        """
        logger.debug("%s started " % cls.__name__)
        cls.api_url = 'http://127.0.0.1:8002/spanglish/word/'
        cls.api_url2 = 'http://127.0.0.1:8002/spanglish/words/'

        # create permissions
        # first get the contenttype of the model
        content_type = ContentType.objects.get_for_model(Word)
        add_permission, created = Permission.objects.get_or_create(
            codename='add_word',
            name='Can add word',
            content_type=content_type
        )
        change_permission, created = Permission.objects.get_or_create(
            codename='change_word',
            name='Can change word',
            content_type=content_type
        )
        delete_permission, created = Permission.objects.get_or_create(
            codename='delete_word',
            name='Can delete word',
            content_type=content_type
        )

        # authenticated user
        username = 'tester'
        password = 'test1234'
        email = 'tester@fedla.net'
        groupName = 'Spanglish'

        # unauthenticated user
        username2 = 'tester2'
        password2 = 'test12342'
        email2 = 'tester2@fedla.net'
        groupName2 = 'Spanglish2'

        # create users
        user = User.objects.create_user(username=username, email=email, password=password)
        user2 = User.objects.create_user(username=username2, email=email2, password=password2)
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
                'password': password
            },
            format='json'
        )

        response = request.json()
        logger.debug("response for authentication: %s", response)

        # # token
        token = response['access']

        # # add the token to the api_client header
        cls.api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


    def test_view_get_all_words_200(self):
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


    def test_view_get_word_error_with_unknow_param_404(self):
        """test the get request to the api with an unknown param,
        expects 404 response with content."""

        # set the url for the api with param
        uri = self.api_url + 'all/'
        response = self.api_client.get(uri) # make the request
        status_code = response.status_code

        logger.debug("response: %s" % response)

        self.assertEquals(status_code, 404)


    def test_view_get_word_with_content(self):
        """test the get request to the api to get word id 1.
        expects 200 response with content json value to match
        the name Verb."""

        # set the url for the api with param
        uri = f'{self.api_url}1/'
        response = self.api_client.get(uri) # make the request
        status_code = response.status_code
        content = response.json()

        logger.debug("response content: %s" % content)

        expected_content = {
            'id': 1, 
            'word': 'Hablar', 
            'language': 2, 
            'category': 1, 
            'created': '2021-09-28 13:35:51+0200'
        }

        self.assertEquals(status_code, 200)
        self.assertDictEqual(d1=content, d2=expected_content)


    def test_view_create_word_201(self):
        """post request to create a new word, expect to get back statuscode 201"""

        data = {
            'word': 'ver', 
            'language': 2, 
            'category': 1
        }
        response = self.api_client.post(self.api_url2, data=data)
        status_code = response.status_code
        content = response.content

        logger.debug("response: %s" % response)
        logger.debug("content: %s" % content)

        self.assertEquals(201, status_code)


    def test_view_create_existing_word_400(self):
        """post an existing word"""

        data = {
            'word': 'ir', 
            'language': 2, 
            'category': 1
        }
        response = self.api_client.post(self.api_url2, data=data)
        status_code = response.status_code
        content = response.json()

        logger.debug("response: %s" % response)
        logger.debug("content: %s" % content)

        self.assertEquals(400, status_code)
        self.assertEquals({'word': ['word with this word already exists.']}, content)


    def test_view_put_word_200(self):
        """update a word by calling the put action. expects response 200"""

        uri = f'{self.api_url}2/'
        data = {'language': 2}
        response = self.api_client.patch(uri, data=data)
        status_code = response.status_code
        content = response.content

        logger.debug("response: %s" % response)
        logger.debug("content: %s" % content)

        self.assertEquals(200, status_code)


    def test_view_delete_word_204(self):
        """delete a word and expect 204"""

        uri = f'{self.api_url}3/'
        response = self.api_client.delete(uri, data={})
        status_code = response.status_code

        logger.debug("response: %s" % response.content)

        self.assertEquals(204, status_code)


    @classmethod
    def tearDownClass(cls):
        """remove the user and the group"""

        Permission.objects.all().delete()
        Group.objects.all().delete()
        User.objects.all().delete()