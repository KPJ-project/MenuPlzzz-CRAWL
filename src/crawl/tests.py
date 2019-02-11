import datetime
from django.test import TestCase
from django.utils import timezone

from .models import StoreType

class StoreTypeModelTests(TestCase):

    def test_default_hello_world(self):
        text = "Hello World!"
        self.assertIs(text == "Hello World!", True)


