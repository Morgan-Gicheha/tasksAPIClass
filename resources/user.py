from main import api, fields, Resource,db
from models.usermodel import Users_model, user_schema, users_schema
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)


ns_users = api.namespace("users", description="all tasks regarding users")

# this helps the user know how to input the data
user_model = api.model(
    "User",
    {
        "fullname": fields.String(
            description="Fullname is required", required=True, min_length=2
        ),
        "email": fields.String(description="Your email", required=True, min_length=2),
        "password": fields.String(
            description="Your password", required=True, min_length=2
        ),
    },
)


@ns_users.route("")
class User_list(Resource):


    @api.doc(security="apikey")
    @jwt_required
    def get(self):
        """Use this endpoint to get all users"""

        logged_in_user = Users_model.query.filter_by(
            id=get_jwt_identity()
        ).first()  # quering for logged in user
        if logged_in_user.is_admin == True:
            return users_schema.dump(Users_model.query.all()), 200
        else:
            return {"message": "Admin preveleges required!"}


@ns_users.route("/<int:_id>")
class Users(Resource):
    @api.doc(security="apikey")
    @jwt_required
    def post(self,_id):
        """Use this endpoint to promote a user"""
        logged_in_user = Users_model.query.filter_by(id=get_jwt_identity()).first()  # quering for logged in user
        if logged_in_user.is_admin == True:
            user_to_promote=Users_model.query.filter_by(id=_id).first()
            if user_to_promote:
                user_to_promote.is_admin=True
                db.session.commit()
                return {"message":"User promoted"},200

            else:
                return {"message": "User not found."},404

        else:
            return {"message":"Adimn preeledge"}
            


    @api.doc(security="apikey")
    @jwt_required
    def get(self, _id):
        """Use this endpoin to get one user by id"""
        logged_in_user = Users_model.query.filter_by(id=get_jwt_identity()).first()  # quering for logged in user
        if logged_in_user.is_admin == True:

            queried_user = Users_model.query.filter_by(id=_id).first()
            if queried_user:
                return user_schema.dump(queried_user), 200  # ok
            else:
                return (({"message": "user not found!"}),404)  # The requested resource was not found.
        else:
            return {"message":"Admin prevelges required"}
    
        # print(Users_model.query.all())
        # user = next((filter((lambda x: x["id"] == id), users_list)), None)
        # if user:
        #     return user, 200  # ok	The request was successfully completed.
        # else:
        #     return ({"message": "user not found"},404,)  # The requested resource was not found.

    @api.expect(user_model)
    # @jwt_required
    def put(self, id):
        """edit a user by id"""

        data = api.payload
        user_to_update = Users_model.query.filter_by(id=id).first()
        if user_to_update:
            if u"fullname" in data:
                user_to_update.fullname = data["fullname"]
            if u"email" in data:
                user_to_update.email = data["email"]
            if u"password" in data:
                user_to_update.password = data["password"]
            user_to_update.create()
            return user_schema.dump(user_to_update), 201  # created
        else:
            return ({"message": "User not found"}), 404  # not found

    # @api.deprecated
    @api.doc(security="apikey")
    @jwt_required
    def delete(self, _id):
        """delete a user by id"""
        logged_in_user = Users_model.query.filter_by(id=get_jwt_identity()).first()  # quering for logged in user
        if logged_in_user.is_admin == True:

            user_to_delete = Users_model.query.filter_by(id=_id).first()
            if user_to_delete:
                Users_model.delete_user(id=id)
                return ({"message": "User deleted!"}), 200  # ok
            else:
                return ({"message": "User not found"}), 404  # not found

        else:
            return {"message": "Admin preveleges required for deletion!"}

        # to_delete = next(filter((lambda x: x["id"] == id), users_list), None)
        # if to_delete:
        #     users_list.remove(to_delete)
        #     return {"message": "User deleted"}, 200  # ok
        # else:
        #     return {"message": "user not found"}, 404  # not found
