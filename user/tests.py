from django.test import TestCase
from user.models import User

class UserTests(TestCase):
    fixtures = ['users']

    def test_superuser(self):
        user = User.objects.get(pk=1)
        print(user)