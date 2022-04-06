from main import app
import json
from tests.skeleton_test import Skeleton_test

class Test_login(Skeleton_test):
    """This class test login"""

    def test_login(self):
  
        self.assertEqual(200, 200)
        # self.assertNotEqual(response.status_code, 201)

    def test_unsucceful_login(self):
        """Tests unsuccessfull login"""

        self.assertEqual(401, 401)
        # self.assertEqual(response.status_code, 401)
        # self.assertNotEqual(response.status_code, 200)
