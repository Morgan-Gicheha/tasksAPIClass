from tests.skeleton_test import Skeleton_test
from main import app

class Port_test(Skeleton_test):
    """this is  test to make sure app is running in prt 5000"""
    def setUp(self):
        self.app = app.test_client()
      

    def test_port(self):
        response = self.app.get("http://127.0.0.1:5000/api/doc")
        self.assertEqual(response.status_code,200)ith how things were, Agile's "founding fathers" came up with a manifesto based on 12 principles.

#1 Satisfy Customers Through Early & Continuous Delivery
