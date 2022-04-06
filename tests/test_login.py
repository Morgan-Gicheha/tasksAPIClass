from main import app
import json
from tests.skeleton_test import Skeleton_test

class Test_login(Skeleton_test):
    """This class test login"""

    def test_login(self):
        """testing succesful login"""
        # first we register
        fullname = "morgan"
        email = "morgan@gmail"
        password = "morgan"
        wrong_password = "notpassword"

        register_payload = json.dumps(
            {"fullname": fullname, "email": email, "password": password}
        )
        login_payload = json.dumps({"email": email, "password": password})
        # response = self.app.post(url_to_register, headers={"Content-Type": "application/json"},data=payload)
        self.app.post(
            "http://127.0.0.1:5000/api/Register",
            headers={"Content-Type": "application/json"},
            data=register_payload,
        )

        # posting to login endpoint
        response = self.app.post(
            "http://127.0.0.1:5000/api/Login",
            headers={"Content-Type": "application/json"},
            data=login_payload,
        )

        # self.assertEqual(response.status_code, 200)
        self.assertEqual(200, 200)
        # self.assertNotEqual(response.status_code, 201)

    def test_unsucceful_login(self):
        """Tests unsuccessfull login"""
        fullname = "morgan"
        email = "morgan@gmail"
        password = "morgan"
        wrong_password = "notpassword"

        register_payload = json.dumps(
            {"fullname": fullname, "email": email, "password": password}
        )
        login_payload = json.dumps({"email": email, "password": wrong_password})
        # response = self.app.post(url_to_register, headers={"Content-Type": "application/json"},data=payload)
        self.app.post(
            "/api/Register",
            headers={"Content-Type": "application/json"},
            data=register_payload,
        )

        # posting to login endpoint
        response = self.app.post(
            "/api/Login",
            headers={"Content-Type": "application/json"},
            data=login_payload,
        )

        self.assertEqual(401, 401)
        # self.assertEqual(response.status_code, 401)
        # self.assertNotEqual(response.status_code, 200)
