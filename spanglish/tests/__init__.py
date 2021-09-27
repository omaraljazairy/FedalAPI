"""Run before the tests to load the fixtures."""
from __future__ import print_function
from django.conf import settings
from django.core.management import call_command
import warnings
# from django.core.cache import cache

warnings.filterwarnings('ignore', category=RuntimeWarning)


def setUpModule():
    """Run before any test in the package runs."""
    print("setup module spanglish is running")
    print("settings.FIXTURES ", settings.FIXTURES)

    # cache.delete_pattern("*")
    spanglish_fixtures = settings.FIXTURES['spanglish']
    # print("spanglish_fixtures: ", spanglish_fixtures)
    call_command('loaddata', spanglish_fixtures, verbosity=1)


def tearDownModule():
    """Clear all the tests."""
    print("teardown module spanglish is done")