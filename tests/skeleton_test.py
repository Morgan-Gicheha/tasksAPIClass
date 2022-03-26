import unittest
import json
from configs.config import TestingConfig
from main import app,db

app.config.from_object(TestingConfig)
class Skeleton_test(unittest.TestCase):
    """This is a skeleton for all all tests"""
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        """teardown method deletes all record after test is run"""
        db.session.remove()
        db.drop_all()
        db.create_all()
