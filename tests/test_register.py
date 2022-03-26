from tests.skeleton_test import Skeleton_test
from main import app
import json

class Register_test(Skeleton_test):
    """Class to test user registration"""
    def test_registration(self):
        """testing succesfull registration"""
        # register credentials
        fullname = "morgan"
        email = "morgan@gmail.com"
        password = "password"

        payload = json.dumps({"fullname":fullname, "email":email,"password":password})

        # response = self.app.post(url_to_register, headers={"Content-Type": "application/json"},data=payload)
        response = self.app.post("http://127.0.0.1:5000/api/Register", headers={"Content-Type": "application/json"},data=payload)
        self.assertEqual(response.status_code,201)
        
    
    
    def test_bad_registration(self):
        """testing succesfull registration"""
        # register credentials
        fullname = "morgan"
        email = "morgan@gmail.com"
        password = ""
        

        payload = json.dumps({"fullname":fullname, "email":email,"password":password})

        # response = self.app.post(url_to_register, headers={"Content-Type": "application/json"},data=payload)
        response = self.app.post("http://127.0.0.1:5000/api/Register", headers={"Content-Type": "application/json"},data=payload)
        self.assertEqual(response.status_code,201)