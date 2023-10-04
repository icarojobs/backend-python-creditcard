import sys

sys.path.append('../../')

import unittest
import fastapi
from fastapi import Depends
from app.depends import get_db_session


class TestUnitDepends(unittest.TestCase):
    def test_get_db_session_method_a_fastapi_depends(self):
        session = Depends(get_db_session)
        self.assertTrue(isinstance(session, type(fastapi.Depends())))
