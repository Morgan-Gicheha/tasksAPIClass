from tests.skeleton_test import Skeleton_test
from main import app
import json
import ast


class Post_task_test(Skeleton_test):
    """This test tests posting tasks"""
    def test_post_task(self):

        fullname = "morgan"
        email = "morgan@gmail"
        password= "morgan"
        wrong_password="notpassword"

        register_payload=json.dumps({"fullname":fullname,"email":email,"password":password})
        login_payload = json.dumps({"email":email,"password":password})
         # response = self.app.post(url_to_register, headers={"Content-Type": "application/json"},data=payload)
        self.app.post("/api/Register",headers={"Content-Type": "application/json"}, data= register_payload)

        # posting to login endpoint
        response=self.app.post("/api/Login",headers={"Content-Type": "application/json"},data=login_payload)
        # print(response.__dict__)
        li=[]
        response_dict=ast.literal_eval((response._get_data_for_json(li)).decode("utf-8"))
        
        token=response_dict["access_token"]

        test_task= {"title":"string","description": "string"}
        test_task2 ={"title":"string2","description":"string2"}

        self.app.post("/api/tasks",headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"},data=json.dumps(test_task))
        self.app.post("/api/tasks",headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"},data=json.dumps(test_task2))

        get_all_response = self.app.get("/api/tasks",headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"})
        
        self.assertEqual(200,get_all_response.status_code)
        # print(type(get_all_response.get_data(as_text=True)))
