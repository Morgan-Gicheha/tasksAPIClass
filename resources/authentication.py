from main import api, fields, Resource
from models.usermodel import Users_model, user_schema, users_schema
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager,jwt_required,create_access_token,get_jwt_identity

# creating namespace
ns_registration = api.namespace("Register", description="Registration details")
ns_login = api.namespace("Login", description="Login details")

# this helps the user know hoe to input the data
register_model = api.model(
    "User",
    {
        "fullname": fields.String(),
        "email": fields.String(min_length=5),
        "password": fields.String(),
    },
)


login_model = api.model(
    "LoginLCredentials", {"email": fields.String(), "password": fields.String()}
)


@ns_login.route("")

class Login(Resource):
    
    @api.expect(login_model)
    def post(self):
        """use this endpoint to login a user"""
        data = api.payload
        email_check=Users_model.check_if_email_exist(email=data["email"])
        
        if email_check:
            if Users_model.password_check(email= email_check.email,password= data["password"]):
                token = create_access_token(identity=email_check.id)
                
                return ({"access_token":token}),200 #ok
                
            else:
                return ({"message":"inavlid credentials pass"}),401 #Unauthorized
        else:
            return ({"message":"inavlid credentials emali"}),401 #Unauthorized



@ns_registration.route("")
class Register(Resource):
    @api.expect(register_model)
    def post(self):
        """use this endpoint to register a user"""
        data = api.payload
        email_check=Users_model.check_if_email_exist(email=data["email"])
        if email_check:
            return ({"message":"Email aready registered!"}),400 #bad request
        user_to_create = Users_model(
            fullname=data["fullname"],
            email=data["email"],
            password=generate_password_hash(data["password"]),
        )
        user_to_create.create()
        # the below function turns the user to create object into json and return it to the user
        return (
            user_schema.dump(user_to_create),
            201,
        )  # 	A new resource was successfully created.


        return users_schema.dump(Users_model.query.all()), 200  # ok

