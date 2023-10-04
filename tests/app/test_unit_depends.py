import fastapi

from app.helpers.custom_helpers import dd
import sys

sys.path.append('../../')

import unittest
from fastapi import Depends
from app.depends import get_db_session


class TestCalculations(unittest.TestCase):
    def test_get_db_session_method_a_fastapi_depends(self):
        session = Depends(get_db_session)
        self.assertTrue(isinstance(session, type(fastapi.Depends())))
