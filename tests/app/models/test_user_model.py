import sys

sys.path.append('../../../')

from passlib.context import CryptContext
from app.models.user_model import UserModel
import unittest

crypt_context = CryptContext(schemes=['sha256_crypt'])


class TestUserModel(unittest.TestCase):
    def test_user_model_attributes(self):
        user_model = UserModel(
            username="testuser",
            password=crypt_context.hash("password")
        )

        self.assertTrue(type(user_model.username) is str)
        self.assertTrue(type(user_model.password) is str)
        self.assertTrue(len(user_model.username) == 8)
        self.assertTrue(32 <= len(user_model.password) <= 80)
