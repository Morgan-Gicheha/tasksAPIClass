from main import db, ma, fields
from werkzeug.security import check_password_hash


class Users_model(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    is_admin= db.Column(db.Boolean,default=False)
    tasks = db.relationship("Task_model", backref="user", lazy=True)
    # category = db.relationship('Category',backref=db.backref('user', lazy=True))

    def create(self):
        """this method adds to the users table"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_single_user_with_id(cls, id):
        """this method querins for a single user"""
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        else:
            return False


    @classmethod
    def delete_user(cls, id):
        """this method deletes a single  user"""
        user_to_delete = cls.query.filter_by(id=id)
        if user_to_delete.first():
            user_to_delete.delete()
            db.session.commit()
            return True
        else:
            return False


    @classmethod
    def check_if_email_exist(cls,email):
        """this method chcks if email exists"""
        email_check = cls.query.filter_by(email=email).first()
        if email_check:
            return email_check
            return True
        else:
            return False

    @classmethod
    def password_check(cls,email,password):
        email_check = cls.query.filter_by(email=email).first()
        if email_check and check_password_hash(email_check.password,password):
            return True
        else:
            return False



# serializing and deserializing data
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "fullname", "email")


user_schema = UserSchema()  # for one object
users_schema = UserSchema(many=True)
